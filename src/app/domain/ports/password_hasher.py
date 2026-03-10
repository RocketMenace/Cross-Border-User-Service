from typing import Protocol

from app.domain.values import HashPassword, RawPassword


class PasswordHasher(Protocol):
    async def hash(self, *, raw_password: RawPassword) -> HashPassword:
        pass

    async def verify(self, *, raw_password: RawPassword, hashed_password: HashPassword) -> bool:
        pass
