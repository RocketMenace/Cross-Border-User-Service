from typing import TypedDict
from uuid import UUID


class UserCreateContract(TypedDict):
    email: str
    phone: str
    first_name: str
    last_name: str
    middle_name: str
    raw_password: str


class UserResponseContract(TypedDict):
    id: UUID
    email: str
    phone: str
    first_name: str
    last_name: str
    middle_name: str
