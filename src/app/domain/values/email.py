from dataclasses import dataclass

from app.domain.values.base import BaseValueObject


@dataclass(frozen=True, kw_only=True, slots=True, repr=False)
class Email(BaseValueObject):
    value: str

    @staticmethod
    def _validate(*, value: str):
        pass
