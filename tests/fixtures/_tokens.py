from pytest import fixture
from rest_framework_simplejwt.tokens import RefreshToken

from django_auth.models import UserModel


@fixture
def access_token(verified_user_model: UserModel) -> str:
    access_token: str = verified_user_model.tokens()["access"]
    return access_token


@fixture
def refresh_token(verified_user_model: UserModel) -> str:
    refresh_token: str = verified_user_model.tokens()["refresh"]
    return refresh_token


@fixture
def refresh_token_blacklist(verified_user_model: UserModel) -> str:
    token = RefreshToken(verified_user_model.tokens()["refresh"])  # noqa
    token.blacklist()
    return str(token)
