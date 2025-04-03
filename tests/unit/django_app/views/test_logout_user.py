from rest_framework import status
from rest_framework.request import Request

from django_auth.django_app.views import LogoutUserView


class TestCaseLogoutUserView:
    def test_logout_bad_payload_returns_400(
        self,
        logout_user_view: LogoutUserView,
        logout_user_invalid_payload_request: Request,
    ) -> None:
        assert (
            logout_user_view.post(logout_user_invalid_payload_request).status_code
            == status.HTTP_400_BAD_REQUEST
        )
