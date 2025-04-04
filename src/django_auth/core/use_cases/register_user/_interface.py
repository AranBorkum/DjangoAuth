from abc import ABC, abstractmethod

from django_auth.core.repository_interfaces import (
    OneTimePasswordRepositoryInterface,
    UserRepositoryInterface,
)
from django_auth.core.use_cases.register_user._dto import RegisterUserDTO
from django_auth.core.use_cases.register_user._output import (
    RegisterUserOutputInterface,
)


class RegisterUserInterface(ABC):
    @abstractmethod
    def __init__(
        self,
        user_repository: UserRepositoryInterface,
        otp_repository: OneTimePasswordRepositoryInterface,
        output: RegisterUserOutputInterface,
    ) -> None: ...

    @abstractmethod
    def register(self, dto: RegisterUserDTO) -> None: ...
