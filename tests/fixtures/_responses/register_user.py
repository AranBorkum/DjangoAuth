from pytest import fixture
from rest_framework.response import Response
from rest_framework.test import APIClient

from django_auth.core.use_cases.register_user import RegisterUserPayload


@fixture
def register_user_response(register_user_payload: RegisterUserPayload) -> Response:
    return APIClient().post("/auth/register/", register_user_payload)


@fixture
def register_user_invalid_payload_response(
    register_user_invalid_payload: RegisterUserPayload,
) -> Response:
    return APIClient().post("/auth/register/", register_user_invalid_payload)
