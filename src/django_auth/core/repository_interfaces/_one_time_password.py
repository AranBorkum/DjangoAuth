from abc import ABC, abstractmethod
from collections.abc import Callable
from uuid import UUID

from django_auth.core.entities import OneTimePassword


class OneTimePasswordRepositoryInterface(ABC):
    @abstractmethod
    def __init__(self, password_generator: Callable[[], str] | None = None) -> None: ...

    @abstractmethod
    def generate(self, user_id: UUID) -> OneTimePassword: ...

    @staticmethod
    @abstractmethod
    def get_by_one_time_password(one_time_password: str) -> OneTimePassword: ...

    @staticmethod
    @abstractmethod
    def remove_by_one_time_password(one_time_password: str) -> None: ...
