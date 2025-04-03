from unittest.mock import Mock
from urllib.request import Request

from pytest import fixture

from django_auth.core.use_cases.register_user import (
    RegisterUserPayload,
)


@fixture
def register_user_request(
    email: str, password: str, first_name: str, last_name: str
) -> Request:
    return Mock(
        spec=Request,
        data=RegisterUserPayload(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
        ),
    )


@fixture
def register_user_invalid_payload_request(
    password: str, first_name: str, last_name: str
) -> Request:
    return Mock(
        spec=Request,
        data=RegisterUserPayload(
            email="",
            password=password,
            first_name=first_name,
            last_name=last_name,
        ),
    )
