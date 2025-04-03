# type: ignore
from collections.abc import Callable
from typing import Unpack

from django.contrib.auth.base_user import AbstractBaseUser
from pytest import fixture
from rest_framework.request import Request

from django_auth.core.use_cases.login_user import LoginUserPayload
from django_auth.django_app.models import UserModel

type TAuthenticator = Callable[
    [Request, Unpack[LoginUserPayload]], AbstractBaseUser | None
]


@fixture
def authenticator(
    email: str, password: str, first_name: str, last_name: str
) -> TAuthenticator:
    def _authenticator(
        request: Request, **kwargs: Unpack[LoginUserPayload]
    ) -> AbstractBaseUser | None:
        user_model = UserModel(
            email=email,
            first_name=first_name,
            last_name=last_name,
            is_verified=True,
        )
        user_model.set_password(password)
        return user_model

    return _authenticator  # type: ignore


@fixture
def authenticator_unverified_user(
    email: str, password: str, first_name: str, last_name: str
) -> TAuthenticator:
    def _authenticator(
        request: Request, **kwargs: Unpack[LoginUserPayload]
    ) -> AbstractBaseUser | None:
        user_model = UserModel(
            email=email,
            first_name=first_name,
            last_name=last_name,
        )
        user_model.set_password(password)
        return user_model

    return _authenticator  # type: ignore


@fixture
def authenticator_unknown_user(
    email: str, password: str, first_name: str, last_name: str
) -> TAuthenticator:
    def _authenticator(
        request: Request, **kwargs: Unpack[LoginUserPayload]
    ) -> AbstractBaseUser | None:
        return None

    return _authenticator  # type: ignore
