from pytest import mark, raises

from django_auth.core.use_cases.logout_user import LogoutUserOutputStatus
from django_auth.outputs import LogoutUserOutput


class TestCaseLogoutUserOutput:
    @mark.django_db
    def test_blacklist_token(self, refresh_token: str) -> None:
        output = LogoutUserOutput()
        output.blacklist_token(refresh_token=refresh_token)
        assert output.status == LogoutUserOutputStatus.SUCCESS

    @mark.django_db
    def test_blacklist_invalid_token(self, refresh_token_blacklist: str) -> None:
        output = LogoutUserOutput()
        output.blacklist_token(refresh_token=refresh_token_blacklist)
        assert output.status == LogoutUserOutputStatus.FAILED

    def test_status(self) -> None:
        with raises(AssertionError):
            _ = LogoutUserOutput().status
