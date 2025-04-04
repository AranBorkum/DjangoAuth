from collections.abc import Callable

from pytest import mark, raises

from django_auth.models import OneTimePasswordModel, UserModel
from django_auth.repositories import OneTimePasswordRepository


class TestCaseOneTimePasswordRepository:
    @mark.django_db
    def test_generate(
        self,
        unverified_user_model: UserModel,
        one_time_password: str,
        otp_password_generator: Callable[[], str],
    ) -> None:
        otp_repository = OneTimePasswordRepository(
            password_generator=otp_password_generator,
        )
        assert OneTimePasswordModel.objects.count() == 0
        otp_repository.generate(unverified_user_model.id)
        assert OneTimePasswordModel.objects.count() == 1
        otp = OneTimePasswordModel.objects.get(one_time_password=one_time_password)
        assert otp.one_time_password == one_time_password
        assert otp.user.id == unverified_user_model.id

    @mark.django_db
    def test_get_by_password(
        self,
        one_time_password: str,
        one_time_password_model: OneTimePasswordModel,
        unverified_user_model: UserModel,
    ) -> None:
        assert OneTimePasswordModel.objects.count() == 1
        otp = OneTimePasswordRepository.get_by_one_time_password(
            one_time_password=one_time_password
        )
        assert otp.one_time_password == one_time_password
        assert otp.user_id == unverified_user_model.id

    @mark.django_db
    def test_get_password_doesnt_exist(self, one_time_password: str) -> None:
        with raises(OneTimePasswordModel.DoesNotExist):
            OneTimePasswordRepository.get_by_one_time_password(
                one_time_password=one_time_password
            )

    @mark.django_db
    def test_remove_password(
        self, one_time_password_model: OneTimePasswordModel, one_time_password: str
    ) -> None:
        assert OneTimePasswordModel.objects.count() == 1
        OneTimePasswordRepository.remove_by_one_time_password(
            one_time_password=one_time_password
        )
        assert OneTimePasswordModel.objects.count() == 0

    @mark.django_db
    def test_remove_password_doesnt_exist(self, one_time_password: str) -> None:
        assert OneTimePasswordModel.objects.count() == 0
        with raises(AssertionError):
            OneTimePasswordRepository.remove_by_one_time_password(
                one_time_password=one_time_password
            )
