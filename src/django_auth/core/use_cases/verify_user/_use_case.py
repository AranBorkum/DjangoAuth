from django_auth.core.repository_interfaces import (
    OneTimePasswordRepositoryInterface,
    UserRepositoryInterface,
)
from django_auth.core.use_cases.verify_user._dto import VerifyUserDTO
from django_auth.core.use_cases.verify_user._interface import VerifyUserInterface
from django_auth.core.use_cases.verify_user._output import VerifyUserOutputInterface
from django_auth.exceptions import UserAlreadyVerified


class VerifyUser(VerifyUserInterface):
    def __init__(
        self,
        user_repository: UserRepositoryInterface,
        otp_repository: OneTimePasswordRepositoryInterface,
        output: VerifyUserOutputInterface,
    ) -> None:
        self._user_repository = user_repository
        self._otp_repository = otp_repository
        self._output = output

    def verify(self, dto: VerifyUserDTO) -> None:
        try:
            one_time_password = self._otp_repository.get_by_one_time_password(
                one_time_password=dto.one_time_password
            )
            self._user_repository.verify_user_by_id(user_id=one_time_password.user_id)
            self._otp_repository.remove_by_one_time_password(
                one_time_password=dto.one_time_password
            )
            self._output.finalize_verification()
        except UserAlreadyVerified:
            self._output.notify_verification_failure()
