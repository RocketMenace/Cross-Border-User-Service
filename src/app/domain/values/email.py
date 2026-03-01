import re
from dataclasses import dataclass
from re import Pattern
from typing import ClassVar, Final

from app.domain.exceptions import InvalidEmailError
from app.domain.values.base import BaseValueObject


@dataclass(frozen=True, kw_only=True, slots=True, repr=False)
class Email(BaseValueObject):
    MIN_LENGTH: ClassVar[int] = 5
    MAX_LENGTH: ClassVar[int] = 30
    LOCAL_PART_PATTERN: ClassVar[Pattern[str]] = re.compile(r"^[a-zA-Z0-9]+$")
    DOMAIN_PART_PATTER: ClassVar[Pattern[str]] = re.compile(
        r"""
        ^
        [a-zA-Z0-9]  # Must start with alphanumeric
        ([a-zA-Z0-9-]{0,28}[a-zA-Z0-9])?  # Optional middle part with hyphens
        (\.[a-zA-Z0-9]([a-zA-Z0-9-]{0,28}[a-zA-Z0-9])?)*  # Additional domain parts
        \.[a-zA-Z]{2,}$  # TLD must be at least 2 letters
    """,
        re.VERBOSE,
    )

    value: str

    def __post_init__(self):
        super().__post_init__()

    def _validate(self, *, value: str) -> None:
        if not isinstance(self.value, str):
            raise ValueError(f"Email must be a string, got {type(self.value).__name__}")
        if not self._validate_length(value=value):
            raise InvalidEmailError(
                f"Email length between {self.MIN_LENGTH} to {self.MAX_LENGTH} allowed.",
            )
        self._validate_pattern(value=value)

    def _validate_length(self, *, value: str) -> bool:
        if len(value) in range(self.MIN_LENGTH, self.MAX_LENGTH + 1):
            return True
        return False

    def _validate_pattern(self, *, value: str) -> None:
        if not self.LOCAL_PART_PATTERN.match(value):
            raise InvalidEmailError(
                f"Local part must contain only letters and numbers (a-z, A-Z, 0-9). "
                f"Got: '{value}'",
            )
        if not self.DOMAIN_PART_PATTER.match(value):
            raise ValueError(
                f"Domain should be like 'example.com' or 'sub.example.co.uk'. "
                f"Got: '{value}'",
            )
