from rest_framework import status
from rest_framework.request import Request

from django_auth.views import RegisterUserView


class TestCaseRegisterUserView:
    def test_view_bad_payload_returns_400(
        self,
        register_user_view: RegisterUserView,
        register_user_invalid_payload_request: Request,
    ) -> None:
        assert (
            register_user_view.post(register_user_invalid_payload_request).status_code
            == status.HTTP_400_BAD_REQUEST
        )
