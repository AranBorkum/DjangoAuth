from django_auth.core.use_cases.logout_user._dto import LogoutUserDTO
from django_auth.core.use_cases.logout_user._interface import LogoutUserInterface
from django_auth.core.use_cases.logout_user._output import LogoutUserOutputInterface


class LogoutUser(LogoutUserInterface):  # type: ignore
    def __init__(self, output: LogoutUserOutputInterface) -> None:
        self._output = output

    def logout(self, dto: LogoutUserDTO) -> None:
        self._output.blacklist_token(refresh_token=dto.refresh_token)
