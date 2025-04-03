from pytest import fixture
from rest_framework.response import Response
from rest_framework.test import APIClient

from django_auth.django_app.models import UserModel


@fixture
def get_user_response(verified_user_model: UserModel) -> Response:
    access_token = verified_user_model.tokens()["access"]
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")
    response = client.get("/auth/me/")
    return response


@fixture
def get_user_invalid_token_response(access_token: str) -> Response:
    client = APIClient()
    access_token = access_token[:-3] + "xxx"
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")
    response = client.get("/auth/me/")
    return response


@fixture
def get_user_no_token_response() -> Response:
    return APIClient().get("/auth/me/")
