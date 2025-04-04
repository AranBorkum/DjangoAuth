from rest_framework import status
from rest_framework.request import Request

from django_auth.views import VerifyUserView


class TestCaseVerifyUserView:
    def test_view_bad_payload_returns_400(
        self,
        verify_user_view: VerifyUserView,
        verify_user_invalid_payload_request: Request,
    ) -> None:
        assert (
            verify_user_view.post(verify_user_invalid_payload_request).status_code
            == status.HTTP_400_BAD_REQUEST
        )
