from django_auth.core import entities, repositories
from django_auth.django_app import models


class UserRepository(repositories.UserRepositoryInterface):  # type: ignore[misc]
    def get_user_by_email(self, *, email: str) -> entities.User:
        user_model = models.UserModel.objects.get(email=email)
        return user_model.to_entity()

    def get_user_tokens_by_email(self, *, email: str) -> dict[str, str]:
        user_model = models.UserModel.objects.get(email=email)
        assert user_model.is_verified
        tokens: dict[str, str] = user_model.tokens()
        return tokens
