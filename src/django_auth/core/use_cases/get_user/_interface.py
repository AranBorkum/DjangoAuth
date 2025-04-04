from abc import ABC, abstractmethod

from django_auth.core.repository_interfaces import UserRepositoryInterface
from django_auth.core.use_cases.get_user._dto import GetUserDTO
from django_auth.core.use_cases.get_user._output import GetUserOutputInterface


class GetUserInterface(ABC):
    @abstractmethod
    def __init__(
        self, repository: UserRepositoryInterface, output: GetUserOutputInterface
    ) -> None: ...

    @abstractmethod
    def retrieve(self, dto: GetUserDTO) -> None: ...
