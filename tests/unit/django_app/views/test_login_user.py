from urllib.request import Request

from rest_framework import status

from django_auth.django_app import views


class TestCaseLoginUserView:
    def test_view_bad_payload_returns_400(
        self,
        login_user_view: views.LoginUserView,
        login_user_invalid_payload_request: Request,
    ) -> None:
        assert (
            login_user_view.post(login_user_invalid_payload_request).status_code
            == status.HTTP_400_BAD_REQUEST
        )
