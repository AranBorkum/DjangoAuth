from collections.abc import Callable

import pytest

from django_auth.django_app import models, repositories


class TestOneTimePasswordRepository:
    @pytest.mark.django_db
    def test_generate(
        self,
        unverified_user_model: models.UserModel,
        one_time_password: str,
        otp_password_generator: Callable[[], str],
    ) -> None:
        otp_repository = repositories.OneTimePasswordRepository(
            password_generator=otp_password_generator
        )
        assert models.OneTimePasswordModel.objects.count() == 0
        otp_repository.generate(user_id=unverified_user_model.id)
        assert models.OneTimePasswordModel.objects.count() == 1
        otp = models.OneTimePasswordModel.objects.get(
            one_time_password=one_time_password
        )
        assert otp.one_time_password == one_time_password
        assert otp.user.id == unverified_user_model.id
