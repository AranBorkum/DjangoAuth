from pytest import mark, raises

from django_auth.models import UserModel
from django_auth.outputs import GetUserOutput


class TestCaseGetUserOutput:
    @mark.django_db
    def test_get_user(self, verified_user_model: UserModel) -> None:
        output = GetUserOutput()
        output.finalize(user=verified_user_model.to_entity())
        assert output.user["first_name"] == verified_user_model.first_name
        assert output.user["last_name"] == verified_user_model.last_name
        assert output.user["email"] == verified_user_model.email
        assert output.user["is_active"] == verified_user_model.is_active
        assert output.user["is_verified"] == verified_user_model.is_verified
        assert output.user["date_joined"] == verified_user_model.date_joined.isoformat()
        assert output.user["last_login"] == verified_user_model.last_login.isoformat()
        assert output.user["id"] == str(verified_user_model.id)

    def test_get_user_user(self) -> None:
        with raises(AssertionError):
            output = GetUserOutput()
            _ = output.user
