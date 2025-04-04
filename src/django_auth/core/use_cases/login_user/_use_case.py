from django_auth.core.use_cases.login_user._dto import LoginUserDTO
from django_auth.core.use_cases.login_user._interface import LoginUserInterface
from django_auth.core.use_cases.login_user._output import LoginUserOutputInterface


class LoginUser(LoginUserInterface):
    def __init__(self, output: LoginUserOutputInterface) -> None:
        self._output = output

    def login(self, dto: LoginUserDTO) -> None:
        self._output.generate_jwt(email=dto.email)
