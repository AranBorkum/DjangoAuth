from pytest import fixture

from django_auth.core.repository_interfaces import (
    OneTimePasswordRepositoryInterface,
    UserRepositoryInterface,
)
from django_auth.django_app.views import VerifyUserView


@fixture
def verify_user_view(
    user_repository: UserRepositoryInterface,
    one_time_password_repository: OneTimePasswordRepositoryInterface,
) -> VerifyUserView:
    return VerifyUserView(
        user_repository=user_repository, otp_repository=one_time_password_repository
    )
