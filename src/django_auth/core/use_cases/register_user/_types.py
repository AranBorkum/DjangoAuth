from enum import Enum, auto
from typing import TypedDict


class RegisterUserOutputType(Enum):
    SUCCESS = auto()
    FAILURE = auto()


class RegisterUserPayload(TypedDict):
    first_name: str
    last_name: str
    email: str
    password: str
