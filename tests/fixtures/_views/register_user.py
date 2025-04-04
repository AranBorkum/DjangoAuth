from pytest import fixture

from django_auth.core.repository_interfaces import (
    OneTimePasswordRepositoryInterface,
    UserRepositoryInterface,
)
from django_auth.views import RegisterUserView


@fixture
def register_user_view(
    user_repository: UserRepositoryInterface,
    one_time_password_repository: OneTimePasswordRepositoryInterface,
) -> RegisterUserView:
    return RegisterUserView(
        user_repository=user_repository, otp_repository=one_time_password_repository
    )


@fixture
def register_user_exists_view(
    user_exists_repository: UserRepositoryInterface,
    one_time_password_repository: OneTimePasswordRepositoryInterface,
) -> RegisterUserView:
    return RegisterUserView(
        user_repository=user_exists_repository,
        otp_repository=one_time_password_repository,
    )
