from collections.abc import Callable
from typing import Any, Unpack

from django.contrib.auth.base_user import AbstractBaseUser
from rest_framework.request import Request
from rest_framework.serializers import (
    CharField,
    EmailField,
    Serializer,
    ValidationError,
)

from django_auth.core.use_cases.login_user import LoginUserDTO, LoginUserPayload
from django_auth.models import UserModel

type TAuthenticator = Callable[
    [Request, Unpack[LoginUserPayload]], AbstractBaseUser | None
]


class LoginUserSerializer(Serializer):
    def __init__(
        self,
        authenticator: TAuthenticator,
        **kwargs: Any,
    ):
        super().__init__(**kwargs)
        self._authenticator = authenticator

    email = EmailField(max_length=255, min_length=6)
    password = CharField(max_length=68, write_only=True)

    def validate(self, attrs: dict[str, str]) -> dict[str, Any]:
        email = attrs.get("email")
        password = attrs.get("password")
        request = self.context.get("request")
        assert isinstance(request, Request)
        user: UserModel | AbstractBaseUser | None = self._authenticator(
            request, **{"email": email, "password": password}
        )
        if not user:
            raise ValidationError("Invalid login credentials")

        if not user.is_verified:  # type: ignore[union-attr]
            raise ValidationError("User is not verified")

        return attrs

    def to_dto(self) -> LoginUserDTO:
        return LoginUserDTO(
            email=self.validated_data["email"],
            password=self.validated_data["password"],
        )
