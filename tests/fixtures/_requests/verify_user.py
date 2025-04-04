from unittest.mock import Mock
from urllib.request import Request

from pytest import fixture

from django_auth.core.use_cases.verify_user import VerifyUserPayload


@fixture
def verify_user_invalid_payload_request() -> Request:
    return Mock(
        spec=Request,
        data=VerifyUserPayload(one_time_password=""),
    )
