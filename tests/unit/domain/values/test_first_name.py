from dataclasses import FrozenInstanceError

import pytest

from app.domain.exceptions.first_name import InvalidFirstNameError
from app.domain.values import FirstName


@pytest.mark.asyncio
async def test_first_name_created_successfully():
    first_name = FirstName(value="Bob")
    assert first_name.value == "Bob"


@pytest.mark.asyncio
async def test_frozen_first_name_value_object():
    first_name = FirstName(value="Bob")
    with pytest.raises(FrozenInstanceError):
        first_name.value = "Mark"


@pytest.mark.asyncio
async def test_first_name_invalid_format():
    with pytest.raises(InvalidFirstNameError):
        FirstName(value="bob")


@pytest.mark.asyncio
async def test_first_name_invalid_min_length():
    with pytest.raises(InvalidFirstNameError):
        FirstName(value="b")


@pytest.mark.asyncio
async def test_first_name_invalid_max_length():
    with pytest.raises(InvalidFirstNameError):
        FirstName(value="dsjfhnsjdfnjsdnfjsdnfdfsdfsdfsdfsdfsddfs")


@pytest.mark.asyncio
async def test_first_name_invalid_value():
    with pytest.raises(InvalidFirstNameError):
        FirstName(value="23Mark")
