from django_auth.core.repository_interfaces._one_time_password import (
    OneTimePasswordRepositoryInterface,
)
from django_auth.core.repository_interfaces._user import UserRepositoryInterface

__all__ = ["UserRepositoryInterface", "OneTimePasswordRepositoryInterface"]
