from pytest import fixture

from django_auth.core.use_cases.login_user import types


@fixture
def login_user_payload(email: str, password: str) -> types.LoginUserPayload:
    return types.LoginUserPayload(email=email, password=password)


@fixture
def login_user_invalid_payload(password: str) -> types.LoginUserPayload:
    return types.LoginUserPayload(email="", password=password)
