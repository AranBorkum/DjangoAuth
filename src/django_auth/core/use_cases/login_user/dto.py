import dataclasses


@dataclasses.dataclass(frozen=True)
class LoginUserDTO:
    email: str
    password: str
