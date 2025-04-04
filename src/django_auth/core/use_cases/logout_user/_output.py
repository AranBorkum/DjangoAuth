from abc import ABC, abstractmethod

from django_auth.core.use_cases.logout_user._types import LogoutUserOutputStatus


class LogoutUserOutputInterface(ABC):
    @property
    @abstractmethod
    def status(self) -> LogoutUserOutputStatus: ...

    @abstractmethod
    def blacklist_token(self, refresh_token: str) -> None: ...
