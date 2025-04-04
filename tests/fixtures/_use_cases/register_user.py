from pytest import fixture

from django_auth.core.repository_interfaces import (
    OneTimePasswordRepositoryInterface,
    UserRepositoryInterface,
)
from django_auth.core.use_cases.register_user import (
    RegisterUser,
    RegisterUserInterface,
    RegisterUserOutputInterface,
)


@fixture
def register_user_use_case(
    user_repository: UserRepositoryInterface,
    register_user_output: RegisterUserOutputInterface,
    one_time_password_repository: OneTimePasswordRepositoryInterface,
) -> RegisterUserInterface:
    return RegisterUser(
        user_repository=user_repository,
        otp_repository=one_time_password_repository,
        output=register_user_output,
    )


@fixture
def register_user_already_exists_use_case(
    user_exists_repository: UserRepositoryInterface,
    register_user_output: RegisterUserOutputInterface,
    one_time_password_repository: OneTimePasswordRepositoryInterface,
) -> RegisterUserInterface:
    return RegisterUser(
        user_repository=user_exists_repository,
        otp_repository=one_time_password_repository,
        output=register_user_output,
    )
