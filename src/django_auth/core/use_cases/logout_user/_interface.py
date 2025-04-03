from abc import ABC, abstractmethod

from django_auth.core.use_cases.logout_user._dto import LogoutUserDTO


class LogoutUserInterface(ABC):
    @abstractmethod
    def __init__(self) -> None: ...

    @abstractmethod
    def logout(self, dto: LogoutUserDTO) -> None: ...
