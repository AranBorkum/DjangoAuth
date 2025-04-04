from dataclasses import dataclass


@dataclass(frozen=True)
class LogoutUserDTO:
    refresh_token: str
