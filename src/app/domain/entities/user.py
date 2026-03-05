from typing import Any

from app.domain.values import Email, FirstName, LastName, MiddleName, Phone, UserID


class UserEntity:
    def __init__(
        self,
        *,
        user_id: UserID,
        email: Email,
        phone: Phone,
        first_name: FirstName,
        last_name: LastName,
        middle_name: MiddleName,
    ):
        self.user_id = user_id
        self.email = email
        self.phone = phone
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name

    def __setattr__(self, key: str, value: Any) -> None:
        if key == "user_id" and getattr(self, "user_id", None) is not None:
            raise AttributeError("Changing entity ID is not permitted")
        object.__setattr__(self, key, value)

    def __eq__(self, other) -> bool:
        if isinstance(other, UserEntity):
            return other.user_id == self.user_id
        return NotImplemented
