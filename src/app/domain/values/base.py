from dataclasses import dataclass, field


@dataclass(frozen=True, kw_only=True, slots=True, repr=False)
class BaseValueObject:
    value: str

    def __post_init__(self):
        self._validate(value=self.value)

    def _validate(self, *, value: str):
        raise NotImplementedError("Child object should implement this method")
