import jwt
import pytest
from django.conf import settings
from rest_framework import response, status

from django_auth.django_app import models


class TestCaseLoginUserView:
    @pytest.mark.django_db
    def test_view_returns_200(self, login_user_response: response.Response) -> None:
        assert login_user_response.status_code == status.HTTP_200_OK

    @pytest.mark.django_db
    def test_view_returns_valid_jwt(
        self,
        login_user_response: response.Response,
        email: str,
        full_name: str,
        verified_user_model: models.UserModel,
    ) -> None:
        response_data = login_user_response.data
        assert isinstance(response_data, dict)
        assert response_data["email"] == email
        assert response_data["full_name"] == full_name
        assert jwt.decode(
            response_data["access_token"],
            settings.SIMPLE_JWT["SIGNING_KEY"],
            algorithms=[settings.SIMPLE_JWT["ALGORITHM"]],
        )["user_id"] == str(verified_user_model.id)
        assert jwt.decode(
            response_data["refresh_token"],
            settings.SIMPLE_JWT["SIGNING_KEY"],
            algorithms=[settings.SIMPLE_JWT["ALGORITHM"]],
        )["user_id"] == str(verified_user_model.id)

    @pytest.mark.django_db
    def test_invalid_payload_returns_400(
        self, login_user_invalid_payload_response: response.Response
    ) -> None:
        assert (
            login_user_invalid_payload_response.status_code
            == status.HTTP_400_BAD_REQUEST
        )

    @pytest.mark.django_db
    def test_valid_payload_unverified_user(
        self, login_unverified_user_response: response.Response
    ) -> None:
        assert login_unverified_user_response.status_code == status.HTTP_400_BAD_REQUEST
