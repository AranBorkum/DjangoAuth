from pytest import mark
from rest_framework import status
from rest_framework.response import Response


class TestLogoutUserView:
    @mark.django_db
    def test_logout_returns_204(self, logout_user_response: Response) -> None:
        assert logout_user_response.status_code == status.HTTP_204_NO_CONTENT

    @mark.django_db
    def test_logout_user_invalid_token(
        self, logout_user_invalid_token_response: Response
    ) -> None:
        assert (
            logout_user_invalid_token_response.status_code
            == status.HTTP_400_BAD_REQUEST
        )

    @mark.django_db
    def test_logout_user_invalid_auth(
        self, logout_user_invalid_auth_response: Response
    ) -> None:
        assert (
            logout_user_invalid_auth_response.status_code
            == status.HTTP_401_UNAUTHORIZED
        )
