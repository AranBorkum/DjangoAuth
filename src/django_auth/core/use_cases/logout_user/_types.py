from enum import Enum, auto
from typing import TypedDict


class LogoutUserOutputStatus(Enum):
    SUCCESS = auto()
    FAILED = auto()


class LogoutUserPayload(TypedDict):
    refresh_token: str
