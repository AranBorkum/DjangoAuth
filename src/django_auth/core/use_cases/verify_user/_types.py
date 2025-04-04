from enum import Enum, auto
from typing import TypedDict


class VerifyUserOutputType(Enum):
    SUCCESS = auto()
    FAILURE = auto()


class VerifyUserPayload(TypedDict):
    one_time_password: str
