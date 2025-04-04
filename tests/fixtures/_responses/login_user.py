from pytest import fixture
from rest_framework.response import Response
from rest_framework.test import APIClient

from django_auth.core.use_cases.login_user import LoginUserPayload
from django_auth.models import UserModel


@fixture
def login_user_response(
    login_user_payload: LoginUserPayload, verified_user_model: UserModel
) -> Response:
    return APIClient().post("/auth/login/", login_user_payload)


@fixture
def login_user_invalid_payload_response(
    login_user_invalid_payload: LoginUserPayload,
) -> Response:
    return APIClient().post("/auth/login/", login_user_invalid_payload)


@fixture
def login_unverified_user_response(
    login_user_payload: LoginUserPayload, unverified_user_model: UserModel
) -> Response:
    return APIClient().post("/auth/login/", login_user_payload)
