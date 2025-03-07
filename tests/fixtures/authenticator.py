# type: ignore
from collections.abc import Callable
from typing import Unpack

import pytest
from django.contrib.auth import base_user
from rest_framework import request

from django_auth.core.use_cases.login_user import types
from django_auth.django_app import models

type TAuthenticator = Callable[
    [request.Request, Unpack[types.LoginUserPayload]], base_user.AbstractBaseUser | None
]


@pytest.fixture
def authenticator(
    email: str, password: str, first_name: str, last_name: str
) -> TAuthenticator:
    def _authenticator(
        request: request.Request, **kwargs: Unpack[types.LoginUserPayload]
    ) -> base_user.AbstractBaseUser | None:
        user_model = models.UserModel(
            email=email,
            first_name=first_name,
            last_name=last_name,
            is_verified=True,
        )
        user_model.set_password(password)
        return user_model

    return _authenticator


@pytest.fixture
def authenticator_unverified_user(
    email: str, password: str, first_name: str, last_name: str
) -> TAuthenticator:
    def _authenticator(
        request: request.Request, **kwargs: Unpack[types.LoginUserPayload]
    ) -> base_user.AbstractBaseUser | None:
        user_model = models.UserModel(
            email=email,
            first_name=first_name,
            last_name=last_name,
        )
        user_model.set_password(password)
        return user_model

    return _authenticator  # type: ignore


@pytest.fixture
def authenticator_unknown_user(
    email: str, password: str, first_name: str, last_name: str
) -> TAuthenticator:
    def _authenticator(
        request: request.Request, **kwargs: Unpack[types.LoginUserPayload]
    ) -> base_user.AbstractBaseUser | None:
        return None

    return _authenticator  # type: ignore
