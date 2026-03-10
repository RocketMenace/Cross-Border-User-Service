import asyncio
import base64
import hashlib
import hmac
from contextlib import asynccontextmanager
from typing import AsyncGenerator

import bcrypt

from app.domain.values import HashPassword, RawPassword
from app.infrastructure.adapters.types import HasherSemaphore, HasherThreadPoolExecutor
from app.infrastructure.exceptions import PasswordHasherError


class BcryptPasswordHasher:
    def __init__(
        self,
        *,
        pepper: bytes,
        work_factor: int,
        executor: HasherThreadPoolExecutor,
        semaphore: HasherSemaphore,
        semaphore_timeout: float,
    ):
        self._pepper = pepper
        self._work_factor = work_factor
        self._executor = executor
        self._semaphore = semaphore
        self._semaphore_timeout = semaphore_timeout

    async def hash(self, *, raw_password: RawPassword) -> HashPassword:
        async with self._permit():
            loop = asyncio.get_running_loop()
            return await loop.run_in_executor(
                self._executor,
                self.hash_sync,
                raw_password,
            )

    async def verify(self, *, raw_password: RawPassword, hashed_password: HashPassword) -> bool:
        async with self._permit():
            loop = asyncio.get_running_loop()
            return await loop.run_in_executor(
                self._executor,
                self.verify_sync,
                raw_password,
                hashed_password,
            )

    def hash_sync(self, raw_password: RawPassword) -> HashPassword:
        base64_hmac_peppered = self._add_pepper(raw_password=raw_password, pepper=self._pepper)
        salt = bcrypt.gensalt(rounds=self._work_factor)
        return HashPassword(value=bcrypt.hashpw(base64_hmac_peppered, salt=salt))

    def verify_sync(self, raw_password: RawPassword, hashed_password: HashPassword) -> bool:
        base64_hmac_peppered = self._add_pepper(raw_password=raw_password, pepper=self._pepper)
        return bcrypt.checkpw(base64_hmac_peppered, hashed_password.value)

    @asynccontextmanager
    async def _permit(self) -> AsyncGenerator[None, None]:
        try:
            await asyncio.wait_for(self._semaphore.acquire(), timeout=self._semaphore_timeout)
        except TimeoutError:
            raise PasswordHasherError(message="Password hasher is busy") from None
        try:
            yield
        finally:
            self._semaphore.release()

    @staticmethod
    def _add_pepper(*, raw_password: RawPassword, pepper: bytes) -> bytes:
        hmac_password = hmac.new(
            key=pepper,
            msg=raw_password.value.encode(),
            digestmod=hashlib.sha384,
        ).digest()
        return base64.b64encode(hmac_password)
