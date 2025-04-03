from uuid import UUID

from django_auth.core.entities import User
from django_auth.core.repository_interfaces import UserRepositoryInterface
from django_auth.django_app.exceptions import UserAlreadyVerified
from django_auth.django_app.models import UserModel


class UserRepository(UserRepositoryInterface):  # type: ignore
    @staticmethod
    def create_user(
        email: str,
        password: str,
        first_name: str,
        last_name: str,
    ) -> User:
        user_model = UserModel.objects.create_user(
            email=email, password=password, first_name=first_name, last_name=last_name
        )
        return user_model.to_entity()

    @staticmethod
    def exists(email: str) -> bool:
        exists: bool = UserModel.objects.filter(email=email).exists()
        return exists

    @staticmethod
    def verify_user_by_id(user_id: UUID) -> None:
        user_model = UserModel.objects.select_for_update().get(id=user_id)
        if user_model.is_verified:
            raise UserAlreadyVerified
        user_model.is_verified = True
        user_model.save()

    @staticmethod
    def get_user_by_email(email: str) -> User:
        user_model = UserModel.objects.get(email=email)
        return user_model.to_entity()

    @staticmethod
    def get_user_by_user_id(user_id: UUID) -> User:
        user_model = UserModel.objects.get(id=user_id)
        return user_model.to_entity()

    @staticmethod
    def get_user_tokens_by_email(email: str) -> dict[str, str]:
        user_model = UserModel.objects.get(email=email)
        assert user_model.is_verified
        tokens: dict[str, str] = user_model.tokens()
        return tokens
