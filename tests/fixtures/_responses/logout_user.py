from pytest import fixture
from rest_framework.response import Response
from rest_framework.test import APIClient

from django_auth.core.use_cases.logout_user import LogoutUserPayload
from django_auth.models import UserModel


@fixture
def logout_user_response(
    verified_user_model: UserModel, logout_verified_user_payload: LogoutUserPayload
) -> Response:
    access_token = verified_user_model.tokens()["access"]
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")
    response = client.post("/auth/logout/", data=logout_verified_user_payload)
    return response


@fixture
def logout_user_invalid_token_response(
    verified_user_model: UserModel, logout_user_payload: LogoutUserPayload
) -> Response:
    access_token = verified_user_model.tokens()["access"]
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")
    response = client.post("/auth/logout/", data=logout_user_payload)
    return response


@fixture
def logout_user_invalid_auth_response(
    logout_verified_user_payload: LogoutUserPayload,
    token: str,
) -> Response:
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
    response = client.post("/auth/logout/", data=logout_verified_user_payload)
    return response
