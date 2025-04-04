from abc import ABC, abstractmethod

from django_auth.core.repository_interfaces import (
    OneTimePasswordRepositoryInterface,
    UserRepositoryInterface,
)
from django_auth.core.use_cases.verify_user._dto import VerifyUserDTO
from django_auth.core.use_cases.verify_user._output import VerifyUserOutputInterface


class VerifyUserInterface(ABC):
    @abstractmethod
    def __init__(
        self,
        user_repository: UserRepositoryInterface,
        otp_repository: OneTimePasswordRepositoryInterface,
        output: VerifyUserOutputInterface,
    ) -> None: ...

    @abstractmethod
    def verify(self, dto: VerifyUserDTO) -> None: ...
