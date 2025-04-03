from pytest import fixture

from django_auth.django_app.models import UserModel


@fixture
def unverified_user_model(
    email: str, password: str, first_name: str, last_name: str
) -> UserModel:
    user_model: UserModel = UserModel.objects.create_user(
        email=email,
        password=password,
        first_name=first_name,
        last_name=last_name,
    )
    return user_model


@fixture
def verified_user_model(
    email: str, password: str, first_name: str, last_name: str
) -> UserModel:
    user_model: UserModel = UserModel.objects.create_user(
        email=email,
        password=password,
        first_name=first_name,
        last_name=last_name,
    )
    user_model.is_verified = True
    user_model.save()
    return user_model
