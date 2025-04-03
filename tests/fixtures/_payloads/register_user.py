from pytest import fixture

from django_auth.core.use_cases.register_user import RegisterUserPayload


@fixture
def register_user_payload(
    email: str, password: str, first_name: str, last_name: str
) -> RegisterUserPayload:
    return RegisterUserPayload(
        email=email,
        password=password,
        first_name=first_name,
        last_name=last_name,
    )


@fixture
def register_user_invalid_payload(
    password: str, first_name: str, last_name: str
) -> RegisterUserPayload:
    return RegisterUserPayload(
        email="",
        password=password,
        first_name=first_name,
        last_name=last_name,
    )
