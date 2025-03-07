import abc

from django_auth.core import entities


class UserRepositoryInterface(abc.ABC):
    @abc.abstractmethod
    def get_user_by_email(self, *, email: str) -> entities.User: ...

    @abc.abstractmethod
    def get_user_tokens_by_email(self, *, email: str) -> dict[str, str]: ...
