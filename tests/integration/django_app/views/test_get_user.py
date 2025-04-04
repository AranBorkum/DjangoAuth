from pytest import mark
from rest_framework import status
from rest_framework.response import Response

from django_auth.models import UserModel


class TestCaseGetUser:
    @mark.django_db
    def test_get_user(
        self, get_user_response: Response, verified_user_model: UserModel
    ) -> None:
        assert get_user_response.status_code == status.HTTP_200_OK
        data = get_user_response.data
        assert isinstance(data, dict)
        assert data["first_name"] == verified_user_model.first_name
        assert data["last_name"] == verified_user_model.last_name
        assert data["email"] == verified_user_model.email
        assert data["is_active"] == verified_user_model.is_active
        assert data["is_verified"] == verified_user_model.is_verified
        assert data["date_joined"] == verified_user_model.date_joined.isoformat()
        assert data["last_login"] == verified_user_model.last_login.isoformat()
        assert data["id"] == str(verified_user_model.id)

    @mark.django_db
    def test_get_user_invalid_token(
        self, get_user_invalid_token_response: Response
    ) -> None:
        assert (
            get_user_invalid_token_response.status_code == status.HTTP_401_UNAUTHORIZED
        )

    @mark.django_db
    def test_get_user_no_token(self, get_user_no_token_response: Response) -> None:
        assert get_user_no_token_response.status_code == status.HTTP_204_NO_CONTENT
