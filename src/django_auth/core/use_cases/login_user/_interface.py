from abc import ABC, abstractmethod

from django_auth.core.use_cases.login_user._dto import LoginUserDTO
from django_auth.core.use_cases.login_user._output import LoginUserOutputInterface


class LoginUserInterface(ABC):
    @abstractmethod
    def __init__(self, output: LoginUserOutputInterface) -> None: ...

    @abstractmethod
    def login(self, dto: LoginUserDTO) -> None: ...
