from pytest import raises

from django_auth.core.use_cases.register_user import (
    RegisterUserDTO,
    RegisterUserOutputType,
)
from django_auth.django_app.outputs import RegisterUserOutput


class TestCaseRegisterUserOutput:
    def test_finalize_creation(self, register_user_dto: RegisterUserDTO) -> None:
        output = RegisterUserOutput()
        output.finalize_creation(register_user_dto)
        assert output.status == RegisterUserOutputType.SUCCESS

    def test_notify_user_exists(self, register_user_dto: RegisterUserDTO) -> None:
        output = RegisterUserOutput()
        output.notify_user_exists(register_user_dto)
        assert output.status == RegisterUserOutputType.FAILURE

    def test_status_not_set(self) -> None:
        output = RegisterUserOutput()
        with raises(AssertionError):
            _ = output.status
