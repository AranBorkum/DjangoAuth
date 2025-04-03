from pytest import fixture

from django_auth.core.use_cases.logout_user import LogoutUserPayload
from django_auth.django_app.models import UserModel


@fixture
def logout_user_payload(token: str) -> LogoutUserPayload:
    return LogoutUserPayload(refresh_token=token)


@fixture
def logout_user_invalid_payload() -> LogoutUserPayload:
    return LogoutUserPayload(refresh_token="")


@fixture
def logout_verified_user_payload(verified_user_model: UserModel) -> LogoutUserPayload:
    refresh_token = verified_user_model.tokens()["refresh"]
    return LogoutUserPayload(refresh_token=refresh_token)
