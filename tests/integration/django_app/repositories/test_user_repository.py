import jwt
import pytest
from django.conf import settings

from django_auth.django_app import models, repositories


class TestUserRepositoryGetUserByEmail:
    @pytest.mark.django_db
    def test_get_user_by_email(
        self, unverified_user_model: models.UserModel, email: str
    ) -> None:
        user = repositories.UserRepository().get_user_by_email(email=email)
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

    @pytest.mark.django_db
    def test_get_user_by_email_user_does_not_exist(self, email: str) -> None:
        with pytest.raises(models.UserModel.DoesNotExist):
            repositories.UserRepository().get_user_by_email(email=email)


class TestCaseUserRepositoryGetUserTokensByEmail:
    @pytest.mark.django_db
    def test_get_user_by_email_token(
        self, verified_user_model: models.UserModel, email: str
    ) -> None:
        tokens = repositories.UserRepository().get_user_tokens_by_email(email=email)
        assert tokens

    @pytest.mark.django_db
    def test_get_user_by_email_access_token(
        self, verified_user_model: models.UserModel, email: str
    ) -> None:
        tokens = repositories.UserRepository().get_user_tokens_by_email(email=email)
        assert tokens
        assert tokens["access"]
        access_token_payload = jwt.decode(
            tokens["access"],
            settings.SIMPLE_JWT["SIGNING_KEY"],
            algorithms=[settings.SIMPLE_JWT["ALGORITHM"]],
        )
        assert access_token_payload["user_id"] == str(verified_user_model.id)
        assert access_token_payload["token_type"] == "access"

    @pytest.mark.django_db
    def test_get_user_by_email_refresh_token(
        self, verified_user_model: models.UserModel, email: str
    ) -> None:
        tokens = repositories.UserRepository().get_user_tokens_by_email(email=email)
        assert tokens
        assert tokens["refresh"]
        access_token_payload = jwt.decode(
            tokens["refresh"],
            settings.SIMPLE_JWT["SIGNING_KEY"],
            algorithms=[settings.SIMPLE_JWT["ALGORITHM"]],
        )
        assert access_token_payload["user_id"] == str(verified_user_model.id)
        assert access_token_payload["token_type"] == "refresh"

    @pytest.mark.django_db
    def test_get_tokens_by_email_unverified_user(
        self, unverified_user_model: models.UserModel, email: str
    ) -> None:
        with pytest.raises(AssertionError):
            repositories.UserRepository().get_user_tokens_by_email(email=email)
