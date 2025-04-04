from uuid import UUID

import jwt
from django.conf import settings
from django.db import IntegrityError
from django.utils import timezone
from freezegun import freeze_time
from pytest import mark, raises

from django_auth.core.entities import User
from django_auth.exceptions import UserAlreadyVerified
from django_auth.models import UserModel
from django_auth.repositories import UserRepository


class TestCaseUserRepositoryCreateUser:
    @freeze_time()
    @mark.django_db
    def test_create_user(
        self, email: str, password: str, first_name: str, last_name: str
    ) -> None:
        assert UserModel.objects.count() == 0
        user = UserRepository.create_user(
            email=email, password=password, first_name=first_name, last_name=last_name
        )
        assert UserModel.objects.count() == 1
        assert isinstance(user, User)
        user_model = UserModel.objects.get(email=email)
        assert user_model.first_name == first_name
        assert user_model.last_name == last_name
        assert user_model.email == email
        assert not user.is_verified
        assert not user.is_staff
        assert not user.is_superuser
        assert user.is_active
        assert user.date_joined == timezone.now()
        assert user.last_login == timezone.now()

    @mark.django_db
    def test_create_user_already_exists(
        self, email: str, password: str, first_name: str, last_name: str
    ) -> None:
        assert UserModel.objects.count() == 0
        UserRepository.create_user(
            email=email, password=password, first_name=first_name, last_name=last_name
        )
        assert UserModel.objects.count() == 1
        with raises(IntegrityError):
            UserRepository.create_user(
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name,
            )


class TestCaseUserRepositoryExists:
    @mark.django_db
    def test_exists(
        self, email: str, password: str, first_name: str, last_name: str
    ) -> None:
        assert UserModel.objects.count() == 0
        assert not UserRepository.exists(email=email)
        UserRepository.create_user(
            email=email, password=password, first_name=first_name, last_name=last_name
        )
        assert UserModel.objects.count() == 1
        assert UserRepository.exists(email=email)

    @mark.django_db
    def test_exists_no_model(self, email: str) -> None:
        assert not UserRepository.exists(email=email)


class TestCaseUserRepositoryVerifyUser:
    @mark.django_db
    def test_verify_user(self, unverified_user_model: UserModel) -> None:
        assert UserModel.objects.count() == 1
        assert not unverified_user_model.is_verified
        UserRepository.verify_user_by_id(user_id=unverified_user_model.id)
        assert UserModel.objects.count() == 1
        user_model = UserModel.objects.get(email=unverified_user_model.email)
        assert user_model.is_verified

    @mark.django_db
    def test_verify_user_already_verified(self, verified_user_model: UserModel) -> None:
        with raises(UserAlreadyVerified):
            UserRepository.verify_user_by_id(user_id=verified_user_model.id)


class TestCaseUserRepositoryGetUserByEmail:
    @mark.django_db
    def test_get_user_by_email(
        self, unverified_user_model: UserModel, email: str
    ) -> None:
        user = UserRepository.get_user_by_email(email=email)
        unverified_user = unverified_user_model.to_entity()
        assert user.id == unverified_user.id
        assert user.first_name == unverified_user.first_name
        assert user.last_name == unverified_user.last_name
        assert user.email == unverified_user.email
        assert user.is_active == unverified_user.is_active
        assert user.is_verified == unverified_user.is_verified
        assert user.is_staff == unverified_user.is_staff
        assert user.is_superuser == unverified_user.is_superuser
        assert user.date_joined == unverified_user.date_joined
        assert user.last_login == unverified_user.last_login

    @mark.django_db
    def test_get_user_by_email_user_does_not_exist(self, email: str) -> None:
        with raises(UserModel.DoesNotExist):
            UserRepository.get_user_by_email(email=email)


class TestCaseUserRepositoryGetUserByUserId:
    @mark.django_db
    def test_get_user_by_user_id(self, unverified_user_model: UserModel) -> None:
        user = UserRepository.get_user_by_user_id(user_id=unverified_user_model.id)
        unverified_user = unverified_user_model.to_entity()
        assert user.id == unverified_user.id
        assert user.first_name == unverified_user.first_name
        assert user.last_name == unverified_user.last_name
        assert user.email == unverified_user.email
        assert user.is_active == unverified_user.is_active
        assert user.is_verified == unverified_user.is_verified
        assert user.is_staff == unverified_user.is_staff
        assert user.is_superuser == unverified_user.is_superuser
        assert user.date_joined == unverified_user.date_joined
        assert user.last_login == unverified_user.last_login

    @mark.django_db
    def test_get_user_by_user_id_user_does_not_exist(self, user_id: UUID) -> None:
        with raises(UserModel.DoesNotExist):
            UserRepository.get_user_by_user_id(user_id=user_id)


class TestCaseUserRepositoryGetUserTokensByEmail:
    @mark.django_db
    def test_get_user_by_email_token(
        self, verified_user_model: UserModel, email: str
    ) -> None:
        tokens = UserRepository.get_user_tokens_by_email(email=email)
        assert tokens

    @mark.django_db
    def test_get_user_by_email_access_token(
        self, verified_user_model: UserModel, email: str
    ) -> None:
        tokens = UserRepository.get_user_tokens_by_email(email=email)
        assert tokens
        assert tokens["access"]
        access_token_payload = jwt.decode(
            tokens["access"],
            settings.SIMPLE_JWT["SIGNING_KEY"],
            algorithms=[settings.SIMPLE_JWT["ALGORITHM"]],
        )
        assert access_token_payload["user_id"] == str(verified_user_model.id)
        assert access_token_payload["token_type"] == "access"

    @mark.django_db
    def test_get_user_by_email_refresh_token(
        self, verified_user_model: UserModel, email: str
    ) -> None:
        tokens = UserRepository.get_user_tokens_by_email(email=email)
        assert tokens
        assert tokens["refresh"]
        access_token_payload = jwt.decode(
            tokens["refresh"],
            settings.SIMPLE_JWT["SIGNING_KEY"],
            algorithms=[settings.SIMPLE_JWT["ALGORITHM"]],
        )
        assert access_token_payload["user_id"] == str(verified_user_model.id)
        assert access_token_payload["token_type"] == "refresh"

    @mark.django_db
    def test_get_tokens_by_email_unverified_user(
        self, unverified_user_model: UserModel, email: str
    ) -> None:
        with raises(AssertionError):
            UserRepository.get_user_tokens_by_email(email=email)
