from django_auth.core.use_cases.verify_user import (
    VerifyUserOutputInterface,
    VerifyUserOutputType,
)


class VerifyUserOutput(VerifyUserOutputInterface):  # type: ignore
    _status: VerifyUserOutputType | None = None

    @property
    def status(self) -> VerifyUserOutputType:
        assert self._status
        return self._status

    def finalize_verification(self) -> None:
        self._status = VerifyUserOutputType.SUCCESS

    def notify_verification_failure(self) -> None:
        self._status = VerifyUserOutputType.FAILURE
