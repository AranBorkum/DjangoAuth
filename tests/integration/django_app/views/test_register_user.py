from pytest import mark
from rest_framework import status
from rest_framework.response import Response

from django_auth.models import OneTimePasswordModel, UserModel


class TestCaseRegisterUserView:
    @mark.django_db
    def test_view_returns_201(
        self,
        register_user_response: Response,
        email: str,
        first_name: str,
        last_name: str,
    ) -> None:
        assert register_user_response.status_code == status.HTTP_201_CREATED
        assert UserModel.objects.count() == 1
        user = UserModel.objects.get(email=email)
        assert user.email == email
        assert user.first_name == first_name
        assert user.last_name == last_name
        assert user.is_active
        assert not user.is_superuser
        assert not user.is_staff
        assert not user.is_verified

    @mark.django_db
    def test_view_returns_400(
        self, register_user_invalid_payload_response: Response
    ) -> None:
        assert (
            register_user_invalid_payload_response.status_code
            == status.HTTP_400_BAD_REQUEST
        )
        assert UserModel.objects.count() == 0

    @mark.django_db
    def test_existing_user_view_returns_400(
        self, unverified_user_model: UserModel, register_user_response: Response
    ) -> None:
        assert register_user_response.status_code == status.HTTP_400_BAD_REQUEST

    @mark.django_db
    def test_one_time_password_created(
        self, register_user_response: Response, email: str
    ) -> None:
        assert OneTimePasswordModel.objects.count() == 1
        assert UserModel.objects.count() == 1
        user = UserModel.objects.get(email=email)
        otp = OneTimePasswordModel.objects.first()
        assert otp.user == user

    @mark.django_db
    def test_one_time_password_not_generate_on_failure(
        self, register_user_invalid_payload_response: Response
    ) -> None:
        assert OneTimePasswordModel.objects.count() == 0
