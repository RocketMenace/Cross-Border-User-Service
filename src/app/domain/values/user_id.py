from dataclasses import dataclass, field
from uuid import UUID, uuid4


@dataclass(frozen=True, slots=True, repr=False, kw_only=True)
class UserID:
    value: str = field(default_factory=lambda: str(uuid4()))

    def __post_init__(self):
        self._validate_uuid(value=self.value)

    @staticmethod
    def _validate_uuid(*, value: str):
        assert UUID(value)
