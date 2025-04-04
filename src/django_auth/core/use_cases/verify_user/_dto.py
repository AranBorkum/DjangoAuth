from dataclasses import dataclass


@dataclass(frozen=True)
class VerifyUserDTO:
    one_time_password: str
