import datetime
import json
import typing
import uuid


class User:
    def __init__(
        self,
        first_name: str,
        last_name: str,
        email: str,
        is_active: bool,
        is_verified: bool,
        is_staff: bool,
        is_superuser: bool,
        date_joined: datetime.datetime,
        last_login: datetime.datetime,
        id_: uuid.UUID | None = None,
    ):
        self.id = id_ or uuid.uuid4()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_active = is_active
        self.is_verified = is_verified
        self.is_staff = is_staff
        self.is_superuser = is_superuser
        self.date_joined = date_joined
        self.last_login = last_login

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def to_json(self) -> dict[str, typing.Any]:
        output = {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "is_active": self.is_active,
            "is_verified": self.is_verified,
            "date_joined": self.date_joined.isoformat(),
            "last_login": self.last_login.isoformat(),
            "id": str(self.id),
        }
        assert json.dumps(output)
        return output
