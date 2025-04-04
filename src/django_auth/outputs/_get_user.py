from typing import Any

from django_auth.core.entities import User
from django_auth.core.use_cases.get_user import GetUserOutputInterface


class GetUserOutput(GetUserOutputInterface):
    _user: dict[str, Any] | None = None

    @property
    def user(self) -> dict[str, Any]:
        assert self._user
        return self._user

    def finalize(self, user: User) -> None:
        self._user = user.to_json()
