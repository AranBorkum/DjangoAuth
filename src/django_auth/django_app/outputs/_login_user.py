from django_auth.core.repository_interfaces import UserRepositoryInterface
from django_auth.core.use_cases.login_user import LoginUserOutputInterface
from django_auth.django_app.repositories import UserRepository


class LoginUserOutput(LoginUserOutputInterface):  # type: ignore
    _login_token_response: dict[str, str] | None = None

    def __init__(self, user_repository: UserRepositoryInterface | None = None) -> None:
        self._user_repository = user_repository or UserRepository()

    @property
    def login_token_response(self) -> dict[str, str]:
        assert self._login_token_response
        return self._login_token_response

    def generate_jwt(self, email: str) -> None:
        user = self._user_repository.get_user_by_email(email=email)
        tokens = self._user_repository.get_user_tokens_by_email(email=email)
        self._login_token_response = {
            "email": user.email,
            "full_name": f"{user.first_name} {user.last_name}",
            "access_token": tokens["access"],
            "refresh_token": tokens["refresh"],
        }
