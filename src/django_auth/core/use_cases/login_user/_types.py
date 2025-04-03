from typing import TypedDict


class LoginUserPayload(TypedDict):
    email: str
    password: str
