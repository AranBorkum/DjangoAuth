from collections.abc import Callable
from uuid import UUID

from django_auth.core.entities import OneTimePassword
from django_auth.core.repository_interfaces import OneTimePasswordRepositoryInterface
from django_auth.core.utilities import otp_password_generator
from django_auth.models import OneTimePasswordModel


class OneTimePasswordRepository(OneTimePasswordRepositoryInterface):
    def __init__(self, password_generator: Callable[[], str] | None = None) -> None:
        self._password_generator = password_generator or otp_password_generator

    def generate(self, user_id: UUID) -> OneTimePassword:
        one_time_password_model = OneTimePasswordModel.objects.create(
            one_time_password=self._password_generator(),
            user_id=user_id,
        )
        return one_time_password_model.to_entity()

    @staticmethod
    def get_by_one_time_password(one_time_password: str) -> OneTimePassword:
        one_time_password_model = OneTimePasswordModel.objects.get(
            one_time_password=one_time_password
        )
        return one_time_password_model.to_entity()

    @staticmethod
    def remove_by_one_time_password(one_time_password: str) -> None:
        otp_qs = OneTimePasswordModel.objects.filter(
            one_time_password=one_time_password
        )
        assert otp_qs.count() == 1
        otp_qs.delete()
