from pytest import fixture

from django_auth.django_app.models import OneTimePasswordModel, UserModel


@fixture
def one_time_password_model(
    unverified_user_model: UserModel, one_time_password: str
) -> OneTimePasswordModel:
    return OneTimePasswordModel.objects.create(
        one_time_password=one_time_password,
        user_id=unverified_user_model.id,
    )


@fixture
def one_time_password_verified_user_model(
    verified_user_model: UserModel, one_time_password: str
) -> OneTimePasswordModel:
    return OneTimePasswordModel.objects.create(
        one_time_password=one_time_password,
        user_id=verified_user_model.id,
    )
