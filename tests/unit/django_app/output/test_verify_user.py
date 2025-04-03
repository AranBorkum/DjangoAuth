from pytest import raises

from django_auth.core.use_cases.verify_user import VerifyUserOutputType
from django_auth.django_app.outputs import VerifyUserOutput


class TestCaseVerifyUserOutput:
    def test_finalize_verification(self) -> None:
        output = VerifyUserOutput()
        output.finalize_verification()
        assert output.status == VerifyUserOutputType.SUCCESS

    def test_notify_verification_failure(self) -> None:
        output = VerifyUserOutput()
        output.notify_verification_failure()
        assert output.status == VerifyUserOutputType.FAILURE

    def test_status_not_set(self) -> None:
        output = VerifyUserOutput()
        with raises(AssertionError):
            _ = output.status
