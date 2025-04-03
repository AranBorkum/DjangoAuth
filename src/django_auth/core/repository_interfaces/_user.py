from abc import ABC, abstractmethod
from uuid import UUID

from django_auth.core.entities import User


class UserRepositoryInterface(ABC):
    @staticmethod
    @abstractmethod
    def create_user(
        email: str,
        password: str,
        first_name: str,
        last_name: str,
    ) -> User: ...

    @staticmethod
    @abstractmethod
    def exists(email: str) -> bool: ...

    @staticmethod
    @abstractmethod
    def verify_user_by_id(user_id: UUID) -> None: ...

    @staticmethod
    @abstractmethod
    def get_user_by_email(email: str) -> User: ...

    @staticmethod
    @abstractmethod
    def get_user_by_user_id(user_id: UUID) -> User: ...

    @staticmethod
    @abstractmethod
    def get_user_tokens_by_email(email: str) -> dict[str, str]: ...
