from app.domain.entities.user import UserEntity
from app.domain.ports import PasswordHasher
from app.domain.values import (
    Email,
    FirstName,
    HashPassword,
    LastName,
    MiddleName,
    Phone,
    RawPassword,
    UserID,
)


class UserService:
    def __init__(self, password_hasher: PasswordHasher):
        self._password_hasher = password_hasher

    async def create_user(
        self,
        *,
        email: str,
        phone: str,
        first_name: str,
        last_name: str,
        middle_name: str,
        raw_password: RawPassword,
    ) -> UserEntity:
        hashed_password = await self._password_hasher.hash(raw_password=raw_password)

        return UserEntity(
            user_id=UserID(),
            email=Email(value=email),
            phone=Phone(value=phone),
            first_name=FirstName(value=first_name),
            last_name=LastName(value=last_name),
            middle_name=MiddleName(value=middle_name),
            hashed_password=hashed_password,
        )

    async def is_password_valid(
        self,
        *,
        raw_password: RawPassword,
        hashed_password: HashPassword,
    ) -> bool:
        return await self._password_hasher.verify(
            raw_password=raw_password,
            hashed_password=hashed_password,
        )
