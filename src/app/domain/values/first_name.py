import re
from dataclasses import dataclass
from re import Pattern
from typing import ClassVar

from app.domain.exceptions import InvalidFirstNameError
from app.domain.values.base import BaseValueObject


@dataclass(frozen=True, kw_only=True, slots=True, repr=False)
class FirstName(BaseValueObject):
    MIN_LENGTH: ClassVar[int] = 2
    MAX_LENGTH: ClassVar[int] = 30
    PATTERN: ClassVar[Pattern[str]] = re.compile(
        r"^(?!.*[\s\-']{2})[A-Za-z]+(?:[\s\-'][A-Za-z]+)*$",
    )
    value: str

    def __post_init__(self):
        super().__post_init__()

    def _validate(self, *, value: str):
        if not isinstance(value, str):
            raise ValueError(
                f"First name must be a string, got {type(self.value).__name__}",
            )
        if not self._validate_length(value=value):
            raise InvalidFirstNameError(
                f"""First name length between
{self.MIN_LENGTH} to {self.MAX_LENGTH} allowed.""",
            )

    def _validate_length(self, *, value: str) -> bool:
        if len(value) in range(self.MIN_LENGTH, self.MAX_LENGTH + 1):
            return True
        return False

    def _validate_pattern(self, *, value: str):
        if not value.istitle():
            raise InvalidFirstNameError(f"First name must start with capital letter. Got: {value}")
        if not self.PATTERN.match(value):
            raise InvalidFirstNameError(
                f"""First name must contain
                only letters and hyphens. Got: '{value}'""",
            )
