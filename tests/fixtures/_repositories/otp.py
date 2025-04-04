from collections.abc import Callable
from uuid import UUID

from django.utils import timezone
from pytest import fixture

from django_auth.core.entities import OneTimePassword
from django_auth.core.repository_interfaces import OneTimePasswordRepositoryInterface


@fixture
def one_time_password_repository(
    otp_password_generator: Callable[[], str], user_id: UUID
) -> OneTimePasswordRepositoryInterface:
    class OneTimePasswordRepository(OneTimePasswordRepositoryInterface):
        def __init__(self, password_generator: Callable[[], str] | None = None) -> None:
            self._password_generator = password_generator or otp_password_generator

        def generate(self, user_id: UUID) -> OneTimePassword:
            return OneTimePassword(
                one_time_password=self._password_generator(),
                user_id=user_id,
                created_at=timezone.now(),
            )

        @staticmethod
        def get_by_one_time_password(one_time_password: str) -> OneTimePassword:
            return OneTimePassword(
                one_time_password=one_time_password,
                user_id=user_id,
                created_at=timezone.now(),
            )

        @staticmethod
        def remove_by_one_time_password(one_time_password: str) -> None:
            return

    return OneTimePasswordRepository()
