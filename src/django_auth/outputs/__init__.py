from django_auth.outputs._get_user import GetUserOutput
from django_auth.outputs._login_user import LoginUserOutput
from django_auth.outputs._logout_user import LogoutUserOutput
from django_auth.outputs._register_user import RegisterUserOutput
from django_auth.outputs._verify_user import VerifyUserOutput

__all__ = [
    "RegisterUserOutput",
    "VerifyUserOutput",
    "LoginUserOutput",
    "LogoutUserOutput",
    "GetUserOutput",
]
