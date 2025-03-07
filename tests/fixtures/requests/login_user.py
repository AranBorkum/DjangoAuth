from unittest.mock import Mock

from pytest import fixture
from rest_framework.request import Request

from django_auth.core.use_cases.login_user import types


@fixture
def login_user_request(login_user_payload: types.LoginUserPayload) -> Request:
    return Mock(
        spec=Request,
        data=login_user_payload,
    )


@fixture
def login_user_invalid_payload_request(
    login_user_invalid_payload: types.LoginUserPayload,
) -> Request:
    return Mock(
        spec=Request,
        data=login_user_invalid_payload,
    )
