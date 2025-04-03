from django_auth.core.use_cases.register_user import (
    RegisterUserDTO,
    RegisterUserOutputInterface,
    RegisterUserOutputType,
)


class RegisterUserOutput(RegisterUserOutputInterface):  # type: ignore
    _status: RegisterUserOutputType | None = None

    @property
    def status(self) -> RegisterUserOutputType:
        assert self._status
        return self._status

    def finalize_creation(self, dto: RegisterUserDTO) -> None:
        self._status = RegisterUserOutputType.SUCCESS

    def notify_user_exists(self, dto: RegisterUserDTO) -> None:
        self._status = RegisterUserOutputType.FAILURE
