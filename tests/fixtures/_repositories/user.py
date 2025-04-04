from uuid import UUID

from django.utils import timezone
from pytest import fixture

from django_auth.core.entities import User
from django_auth.core.repository_interfaces import UserRepositoryInterface
from django_auth.models import UserModel


@fixture
def user_repository(
    email: str, password: str, first_name: str, last_name: str, user_id: UUID
) -> UserRepositoryInterface:
    class UserDoesNotExistRepository(UserRepositoryInterface):
        @staticmethod
        def create_user(
            email: str,
            password: str,
            first_name: str,
            last_name: str,
        ) -> User:
            return User(
                email=email,
                first_name=first_name,
                last_name=last_name,
                is_active=True,
                is_verified=False,
                is_staff=False,
                is_superuser=False,
                date_joined=timezone.now(),
                last_login=timezone.now(),
            )

        @staticmethod
        def exists(email: str) -> bool:
            return False

        @staticmethod
        def verify_user_by_id(user_id: UUID) -> None:
            return

        @staticmethod
        def get_user_by_email(email: str) -> User:
            return User(
                id_=user_id,
                email=email,
                first_name=first_name,
                last_name=last_name,
                is_active=True,
                is_verified=True,
                is_staff=False,
                is_superuser=False,
                date_joined=timezone.now(),
                last_login=timezone.now(),
            )

        @staticmethod
        def get_user_by_user_id(user_id: UUID) -> User:
            return User(
                id_=user_id,
                email=email,
                first_name=first_name,
                last_name=last_name,
                is_active=True,
                is_verified=True,
                is_staff=False,
                is_superuser=False,
                date_joined=timezone.now(),
                last_login=timezone.now(),
            )

        @staticmethod
        def get_user_tokens_by_email(email: str) -> dict[str, str]:
            user_model = UserModel(
                id=user_id,
                email=email,
                first_name=first_name,
                last_name=last_name,
                is_verified=True,
            )
            user_model.set_password(password)
            tokens: dict[str, str] = user_model.tokens()
            return tokens

    return UserDoesNotExistRepository()


@fixture
def user_exists_repository() -> UserRepositoryInterface:
    class UserExistsRepository(UserRepositoryInterface):
        @staticmethod
        def create_user(
            email: str,
            password: str,
            first_name: str,
            last_name: str,
        ) -> User:
            raise NotImplementedError()  # pragma: nocover

        @staticmethod
        def exists(email: str) -> bool:
            return True

        @staticmethod
        def verify_user_by_id(user_id: UUID) -> None:
            return

        @staticmethod
        def get_user_by_email(email: str) -> User:
            raise NotImplementedError

        @staticmethod
        def get_user_by_user_id(user_id: UUID) -> User:
            raise NotImplementedError

        @staticmethod
        def get_user_tokens_by_email(email: str) -> dict[str, str]:
            raise NotImplementedError

    return UserExistsRepository()
