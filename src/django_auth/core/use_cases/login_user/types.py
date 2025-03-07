from typing import TypedDict


class LoginUserPayload(TypedDict):
    email: str
    password: str


class LoginUserResponsePayload(TypedDict):
    email: str
    full_name: str
    access_token: str
    refresh_token: str
