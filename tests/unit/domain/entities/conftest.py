import pytest_asyncio

from app.domain.entities.user import UserEntity
from app.domain.values import Email, FirstName, LastName, MiddleName, Phone, UserID


@pytest_asyncio.fixture
async def create_valid_user() -> UserEntity:
    user_id = UserID(value="02d70dc9-643c-47e9-b947-d3350876f747")
    first_name = FirstName(value="Bob")
    middle_name = MiddleName(value="Brown")
    last_name = LastName(value="Josh")
    phone = Phone(value="+789034586523")
    email = Email(value="bobbrown@example.com")
    user = UserEntity(
        user_id=user_id,
        first_name=first_name,
        last_name=last_name,
        middle_name=middle_name,
        phone=phone,
        email=email,
    )
    return user
