from unittest.mock import Mock

from pytest import fixture
from rest_framework.request import Request

from django_auth.core.use_cases.logout_user import LogoutUserPayload


@fixture
def logout_user_invalid_payload_request(
    logout_user_invalid_payload: LogoutUserPayload,
) -> Request:
    return Mock(
        spec=Request,
        data=logout_user_invalid_payload,
    )
