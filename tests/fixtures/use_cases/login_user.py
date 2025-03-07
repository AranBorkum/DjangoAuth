from collections.abc import Callable

import pytest

from django_auth.core import repositories, use_cases


@pytest.fixture
def login_user_use_case(
    user_repository: Callable[[bool, bool], repositories.UserRepositoryInterface],
) -> use_cases.LoginUser:
    repository = user_repository(True, True)
    return use_cases.LoginUser(repository=repository)


@pytest.fixture
def login_user_get_user_failure_use_case(
    user_repository: Callable[[bool, bool], repositories.UserRepositoryInterface],
) -> use_cases.LoginUser:
    repository = user_repository(False, True)
    return use_cases.LoginUser(repository=repository)


@pytest.fixture
def login_user_get_tokens_failure_use_case(
    user_repository: Callable[[bool, bool], repositories.UserRepositoryInterface],
) -> use_cases.LoginUser:
    repository = user_repository(True, False)
    return use_cases.LoginUser(repository=repository)
