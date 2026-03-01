from typing import Any


class UserEntity:
    def __init__(
        self,
        user_id,
        email,
        phone,
        first_name,
        last_name,
        middle_name,
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
