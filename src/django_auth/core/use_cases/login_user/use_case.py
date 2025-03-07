from django_auth.core import repositories
from django_auth.core.use_cases.login_user import dto, types


class LoginUser:
    def __init__(self, repository: repositories.UserRepositoryInterface):
        self._repository = repository

    def __call__(self, login_dto: dto.LoginUserDTO) -> types.LoginUserResponsePayload:
        user = self._repository.get_user_by_email(email=login_dto.email)
        tokens = self._repository.get_user_tokens_by_email(email=user.email)
        return types.LoginUserResponsePayload(
            email=user.email,
            full_name=f"{user.first_name} {user.last_name}",
            access_token=tokens["access"],
            refresh_token=tokens["refresh"],
        )
