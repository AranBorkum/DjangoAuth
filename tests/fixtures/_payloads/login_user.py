from pytest import fixture

from django_auth.core.use_cases.login_user import LoginUserPayload


@fixture
def login_user_payload(email: str, password: str) -> LoginUserPayload:
    return LoginUserPayload(email=email, password=password)


@fixture
def login_user_invalid_payload(password: str) -> LoginUserPayload:
    return LoginUserPayload(email="", password=password)
