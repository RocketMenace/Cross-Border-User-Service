from dataclasses import FrozenInstanceError

import pytest

from app.domain.values import UserID


@pytest.mark.asyncio
async def test_user_id_created_successfully():
    user_id = UserID(value="02d70dc9-643c-47e9-b947-d3350876f747")
    assert user_id.value == "02d70dc9-643c-47e9-b947-d3350876f747"


@pytest.mark.asyncio
async def test_frozen_user_id_value_object():
    user_id = UserID(value="02d70dc9-643c-47e9-b947-d3350876f747")
    with pytest.raises(FrozenInstanceError):
        user_id.value = "02d70dc9-643c-47e9-b947-d3350876f747"


@pytest.mark.asyncio
async def test_user_id_invalid_format():
    with pytest.raises(ValueError):
        UserID(value="02d70dc9-643c-47e9-b947")
