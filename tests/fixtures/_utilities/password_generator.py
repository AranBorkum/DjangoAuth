from collections.abc import Callable

from pytest import fixture


@fixture
def otp_password_generator(one_time_password: str) -> Callable[[], str]:
    def _generator() -> str:
        return one_time_password

    return _generator
