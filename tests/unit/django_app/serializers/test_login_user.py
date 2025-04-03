from collections.abc import Callable
from typing import Any

from django.contrib.auth.base_user import AbstractBaseUser
from rest_framework.request import Request

from django_auth.core.use_cases.login_user import LoginUserDTO, LoginUserPayload
from django_auth.django_app.serializers import LoginUserSerializer


class TestLoginUserSerializer:
    def test_serialize(
        self,
        login_user_payload: LoginUserPayload,
        login_user_request: Request,
        authenticator: Callable[[Request, Any], AbstractBaseUser | None],
    ) -> None:
        assert LoginUserSerializer(
            authenticator=authenticator,
            data=login_user_payload,
            context={"request": login_user_request},
        ).is_valid()

    def test_invalid_payload_serialize(
        self,
        login_user_invalid_payload: LoginUserPayload,
        login_user_invalid_payload_request: Request,
        authenticator: Callable[[Request, Any], AbstractBaseUser | None],
    ) -> None:
        assert not LoginUserSerializer(
            authenticator=authenticator,
            data=login_user_invalid_payload,
            context={"request": login_user_invalid_payload_request},
        ).is_valid()

    def test_unknown_user(
        self,
        login_user_payload: LoginUserPayload,
        login_user_request: Request,
        authenticator_unknown_user: Callable[[Request, Any], AbstractBaseUser | None],
    ) -> None:
        assert not LoginUserSerializer(
            authenticator=authenticator_unknown_user,
            data=login_user_payload,
            context={"request": login_user_request},
        ).is_valid()

    def test_unverified_user(
        self,
        login_user_payload: LoginUserPayload,
        login_user_request: Request,
        authenticator_unverified_user: Callable[
            [Request, Any], AbstractBaseUser | None
        ],
    ) -> None:
        assert not LoginUserSerializer(
            authenticator=authenticator_unverified_user,
            data=login_user_payload,
            context={"request": login_user_request},
        ).is_valid()

    def test_to_dto(
        self,
        email: str,
        password: str,
        login_user_payload: LoginUserPayload,
        login_user_request: Request,
        authenticator: Callable[[Request, Any], AbstractBaseUser | None],
    ) -> None:
        serializer = LoginUserSerializer(
            authenticator=authenticator,
            data=login_user_payload,
            context={"request": login_user_request},
        )
        assert serializer.is_valid()
        dto = serializer.to_dto()
        assert isinstance(dto, LoginUserDTO)
        assert dto.email == email
        assert dto.password == password
