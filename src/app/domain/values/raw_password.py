import re
from dataclasses import dataclass, field
from re import Pattern
from typing import ClassVar

from app.domain.exceptions import InvalidPasswordFormatError
from app.domain.values.base import BaseValueObject


@dataclass(frozen=True, slots=True, repr=False, kw_only=True)
class RawPassword(BaseValueObject):
    MIN_LENGTH: ClassVar[int] = 7
    MAX_LENGTH: ClassVar[int] = 30
    PATTERN: ClassVar[Pattern[str]] = re.compile(
        r"""^(?=.*[A-Z])(?=.*[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?])(?=.*[a-z])(?=.*\d).{7,12}$""",
    )
    value: str

    def __post_init__(self):
        super().__post_init__()

    def _validate(self, *, value: str):
        if not isinstance(value, str):
            raise ValueError(
                f"Password must be a string, got {type(self.value).__name__}",
            )
        if not self._validate_length(value=value):
            raise InvalidPasswordFormatError(
                f"""Password length between
    {self.MIN_LENGTH} to {self.MAX_LENGTH} allowed.""",
            )
        self._validate_pattern(value=value)

    def _validate_pattern(self, *, value: str) -> None:
        if not self.PATTERN.match(value):
            raise InvalidPasswordFormatError(
                f"""Password must contain
                at least one capital letter, special symbol. Got: '{value}'""",
            )

    def _validate_length(self, *, value: str) -> bool:
        if len(value) in range(self.MIN_LENGTH, self.MAX_LENGTH):
            return True
        return False
