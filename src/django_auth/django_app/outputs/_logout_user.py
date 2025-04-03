from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken

from django_auth.core.use_cases.logout_user import (
    LogoutUserOutputInterface,
    LogoutUserOutputStatus,
)


class LogoutUserOutput(LogoutUserOutputInterface):  # type: ignore
    _status: LogoutUserOutputStatus | None = None

    @property
    def status(self) -> LogoutUserOutputStatus:
        assert self._status
        return self._status

    def blacklist_token(self, refresh_token: str) -> None:
        try:
            RefreshToken(refresh_token).blacklist()  # type: ignore
            self._status = LogoutUserOutputStatus.SUCCESS
        except TokenError:
            self._status = LogoutUserOutputStatus.FAILED
