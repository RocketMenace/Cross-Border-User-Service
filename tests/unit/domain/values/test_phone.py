from dataclasses import FrozenInstanceError

import pytest

from app.domain.exceptions.phone import InvalidPhoneError
from app.domain.values import Phone


@pytest.mark.asyncio
async def test_phone_created_successfully():
    phone = Phone(value="+79863456732")
    assert phone.value == "+79863456732"


@pytest.mark.asyncio
async def test_frozen_phone_value_object():
    phone = Phone(value="+79863456732")
    with pytest.raises(FrozenInstanceError):
        phone.value = "+79863456732"


@pytest.mark.asyncio
async def test_phone_invalid_format():
    with pytest.raises(InvalidPhoneError):
        Phone(value="S+79863456732")


@pytest.mark.asyncio
async def test_phone_min_length():
    with pytest.raises(InvalidPhoneError):
        Phone(value="2234")


@pytest.mark.asyncio
async def test_phone_invalid_max_length():
    with pytest.raises(InvalidPhoneError):
        Phone(value="+73742837482375892374823482398048239423")
