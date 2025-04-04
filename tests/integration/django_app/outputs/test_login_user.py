import jwt
from django.conf import settings
from pytest import mark, raises

from django_auth.models import UserModel
from django_auth.outputs import LoginUserOutput
from django_auth.repositories import UserRepository


class TestCaseLoginUserOutput:
    @mark.django_db
    def test_generate_jwt(
        self,
        email: str,
        full_name: str,
        verified_user_model: UserModel,
    ) -> None:
        output = LoginUserOutput(user_repository=UserRepository())
        output.generate_jwt(email=email)
        assert output.login_token_response["email"] == email
        assert output.login_token_response["full_name"] == full_name

        access_token_payload = jwt.decode(
            output.login_token_response["access_token"],
            settings.SIMPLE_JWT["SIGNING_KEY"],
            algorithms=[settings.SIMPLE_JWT["ALGORITHM"]],
        )
        assert access_token_payload["user_id"] == str(verified_user_model.id)

        refresh_token_payload = jwt.decode(
            output.login_token_response["refresh_token"],
            settings.SIMPLE_JWT["SIGNING_KEY"],
            algorithms=[settings.SIMPLE_JWT["ALGORITHM"]],
        )
        assert refresh_token_payload["user_id"] == str(verified_user_model.id)

    def test_login_token_response(
        self,
    ) -> None:
        with raises(AssertionError):
            output = LoginUserOutput()
            _ = output.login_token_response
