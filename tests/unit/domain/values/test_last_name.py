from dataclasses import FrozenInstanceError

import pytest

from app.domain.exceptions.last_name import InvalidLastNameError
from app.domain.values import LastName


@pytest.mark.asyncio
async def test_last_name_created_successfully():
    first_name = LastName(value="Bob")
    assert first_name.value == "Bob"


@pytest.mark.asyncio
async def test_frozen_last_name_value_object():
    last_name = LastName(value="Bob")
    with pytest.raises(FrozenInstanceError):
        last_name.value = "Mark"


@pytest.mark.asyncio
async def test_last_name_invalid_format():
    with pytest.raises(InvalidLastNameError):
        LastName(value="bob")


@pytest.mark.asyncio
async def test_last_name_invalid_min_length():
    with pytest.raises(InvalidLastNameError):
        LastName(value="b")


@pytest.mark.asyncio
async def test_last_name_invalid_max_length():
    with pytest.raises(InvalidLastNameError):
        LastName(value="dsjfhnsjdfnjsdnfjsdnfdfsdfsdfsdfsdfsddfs")


@pytest.mark.asyncio
async def test_last_name_invalid_value():
    with pytest.raises(InvalidLastNameError):
        LastName(value="23Mark")
