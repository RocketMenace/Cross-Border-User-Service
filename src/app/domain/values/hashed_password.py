from dataclasses import dataclass

from app.domain.values.base import BaseValueObject


@dataclass(frozen=True, slots=True, repr=False, kw_only=True)
class HashPassword(BaseValueObject):
    value: bytes
