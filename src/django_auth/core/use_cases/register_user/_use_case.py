from collections.abc import Callable

from django_auth.core.repository_interfaces import (
    OneTimePasswordRepositoryInterface,
    UserRepositoryInterface,
)
from django_auth.core.use_cases.register_user._dto import RegisterUserDTO
from django_auth.core.use_cases.register_user._interface import RegisterUserInterface
from django_auth.core.use_cases.register_user._output import (
    RegisterUserOutputInterface,
)


class RegisterUser(RegisterUserInterface):  # type: ignore
    def __init__(
        self,
        user_repository: UserRepositoryInterface,
        otp_repository: OneTimePasswordRepositoryInterface,
        output: RegisterUserOutputInterface,
    ) -> None:
        self._user_repository = user_repository
        self._otp_repository = otp_repository
        self._output = output

        self._functionality_map: dict[bool, Callable[[RegisterUserDTO], None]] = {
            True: self._handle_user_exists,
            False: self._register_user,
        }

    def _register_user(self, dto: RegisterUserDTO) -> None:
        user = self._user_repository.create_user(
            email=dto.email,
            password=dto.password,
            first_name=dto.first_name,
            last_name=dto.last_name,
        )
        self._otp_repository.generate(user_id=user.id)
        self._output.finalize_creation(dto=dto)

    def _handle_user_exists(self, dto: RegisterUserDTO) -> None:
        self._output.notify_user_exists(dto=dto)

    def register(self, dto: RegisterUserDTO) -> None:
        self._functionality_map[self._user_repository.exists(email=dto.email)](dto)
