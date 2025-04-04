from pytest import mark

from django_auth.core.entities import User
from django_auth.models import UserModel


class TestCaseUserModel:
    @mark.django_db
    def test_to_entity(self, unverified_user_model: UserModel) -> None:
        user: User = unverified_user_model.to_entity()
        assert isinstance(user, User)
        assert user.id == unverified_user_model.id
        assert user.first_name == unverified_user_model.first_name
        assert user.last_name == unverified_user_model.last_name
        assert user.email == unverified_user_model.email
        assert user.is_active == unverified_user_model.is_active
        assert user.is_verified == unverified_user_model.is_verified
        assert user.is_staff == unverified_user_model.is_staff
        assert user.is_superuser == unverified_user_model.is_superuser
        assert user.date_joined == unverified_user_model.date_joined
        assert user.last_login == unverified_user_model.last_login
