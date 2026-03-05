from dataclasses import FrozenInstanceError

import pytest

from app.domain.exceptions.middle_name import InvalidMiddleNameNameError
from app.domain.values import MiddleName


@pytest.mark.asyncio
async def test_middle_name_created_successfully():
    middle = MiddleName(value="Bob")
    assert middle.value == "Bob"


@pytest.mark.asyncio
async def test_frozen_middle_name_value_object():
    middle_name = MiddleName(value="Bob")
    with pytest.raises(FrozenInstanceError):
        middle_name.value = "Mark"


@pytest.mark.asyncio
async def test_middle_name_invalid_format():
    with pytest.raises(InvalidMiddleNameNameError):
        MiddleName(value="bob")


@pytest.mark.asyncio
async def test_middle_name_invalid_min_length():
    with pytest.raises(InvalidMiddleNameNameError):
        MiddleName(value="b")


@pytest.mark.asyncio
async def test_middle_name_invalid_max_length():
    with pytest.raises(InvalidMiddleNameNameError):
        MiddleName(value="dsjfhnsjdfnjsdnfjsdnfdfsdfsdfsdfsdfsddfs")


@pytest.mark.asyncio
async def test_middle_name_invalid_value():
    with pytest.raises(InvalidMiddleNameNameError):
        MiddleName(value="23Mark")


@pytest.mark.asyncio
async def test_middle_name_invalid_char():
    with pytest.raises(InvalidMiddleNameNameError):
        MiddleName(value="Mark#")
