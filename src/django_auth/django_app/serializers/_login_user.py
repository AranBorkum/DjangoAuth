import typing

from django.contrib.auth import base_user
from rest_framework import request, serializers

from django_auth.core.use_cases.login_user import dto, types

type TAuthenticator = typing.Callable[
    [request.Request, typing.Unpack[types.LoginUserPayload]],
    base_user.AbstractBaseUser | None,
]


class LoginUserSerializer(serializers.Serializer):  # type: ignore[misc]
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=255, write_only=True)

    def __init__(self, authenticator: TAuthenticator, **kwargs: typing.Any):
        self._authenticator = authenticator
        super().__init__(**kwargs)

    def validate(self, attrs: dict[str, typing.Any]) -> dict[str, typing.Any]:
        email = attrs.get("email")
        password = attrs.get("password")
        login_request = self.context.get("request")
        assert isinstance(login_request, request.Request)

        user = self._authenticator(
            login_request,
            **{"email": email, "password": password},
        )
        if not user:
            raise serializers.ValidationError("Invalid login credentials")

        if not user.is_verified:  # type: ignore[attr-defined]
            raise serializers.ValidationError("User is not verified")

        return attrs

    def to_dto(self) -> dto.LoginUserDTO:
        return dto.LoginUserDTO(
            email=self.validated_data["email"],
            password=self.validated_data["password"],
        )
