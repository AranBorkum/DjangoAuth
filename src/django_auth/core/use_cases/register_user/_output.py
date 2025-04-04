from abc import ABC, abstractmethod

from django_auth.core.use_cases.register_user._dto import RegisterUserDTO
from django_auth.core.use_cases.register_user._types import RegisterUserOutputType


class RegisterUserOutputInterface(ABC):
    @property
    @abstractmethod
    def status(self) -> RegisterUserOutputType: ...

    @abstractmethod
    def finalize_creation(self, dto: RegisterUserDTO) -> None: ...

    @abstractmethod
    def notify_user_exists(self, dto: RegisterUserDTO) -> None: ...
