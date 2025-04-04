from pytest import mark
from rest_framework import status
from rest_framework.response import Response

from django_auth.models import OneTimePasswordModel


class TestCaseVerifyUserView:
    @mark.django_db
    def test_verify_user(self, verify_user_response: Response) -> None:
        assert verify_user_response.status_code == status.HTTP_200_OK

    @mark.django_db
    def test_verify_user_already_verified(
        self, verify_user_already_verified_response: Response
    ) -> None:
        assert (
            verify_user_already_verified_response.status_code
            == status.HTTP_400_BAD_REQUEST
        )

    @mark.django_db
    def test_verify_user_invalid_payload(
        self, verify_user_invalid_payload_response: Response
    ) -> None:
        assert (
            verify_user_invalid_payload_response.status_code
            == status.HTTP_400_BAD_REQUEST
        )

    @mark.django_db
    def test_otp_deleted_after_successful_verification(
        self, verify_user_response: Response
    ) -> None:
        assert OneTimePasswordModel.objects.count() == 0
