import pytest

from app.domain.entities.user import UserEntity
from app.domain.values import Email, FirstName, HashPassword, LastName, MiddleName, Phone, UserID


@pytest.mark.asyncio
async def test_user_created_successfully():
    user_id = UserID(value="02d70dc9-643c-47e9-b947-d3350876f747")
    first_name = FirstName(value="Bob")
    middle_name = MiddleName(value="Brown")
    last_name = LastName(value="Josh")
    phone = Phone(value="+789034586523")
    email = Email(value="bobbrown@example.com")
    hashed_password = HashPassword(value=b"qwerty")
    user = UserEntity(
        user_id=user_id,
        first_name=first_name,
        last_name=last_name,
        middle_name=middle_name,
        phone=phone,
        email=email,
        hashed_password=hashed_password,
    )

    assert user.first_name.value == "Bob"
    assert user.middle_name.value == "Brown"
    assert user.last_name.value == "Josh"
    assert user.phone.value == "+789034586523"
    assert user.email.value == "bobbrown@example.com"


@pytest.mark.asyncio
async def test_user_cannot_change_identity(create_valid_user):
    user = create_valid_user
    with pytest.raises(AttributeError):
        user.user_id = "3500c110-5f0c-4454-a6db-76c826a78c1a"


@pytest.mark.asyncio
async def test_user_can_change_email(create_valid_user):
    user = create_valid_user
    user.first_name = FirstName(value="Mark")
    assert user.first_name.value == "Mark"
