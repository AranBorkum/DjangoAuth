from abc import ABC, abstractmethod
from typing import Any

from django_auth.core.entities import User


class GetUserOutputInterface(ABC):
    @property
    @abstractmethod
    def user(self) -> dict[str, Any]: ...

    @abstractmethod
    def finalize(self, user: User) -> None: ...
