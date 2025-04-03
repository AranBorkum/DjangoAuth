from abc import ABC, abstractmethod


class LoginUserOutputInterface(ABC):
    @property
    @abstractmethod
    def login_token_response(self) -> dict[str, str]: ...

    @abstractmethod
    def generate_jwt(self, email: str) -> None: ...
