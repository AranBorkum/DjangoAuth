import uuid

from django.contrib.auth import base_user
from django.contrib.auth import models as auth_models
from django.core.validators import validate_email
from django.db import models
from rest_framework_simplejwt import tokens

from django_auth.core.entities import User


class _UserManager(base_user.BaseUserManager):  # type: ignore
    def create_user(
        self, email: str, first_name: str, last_name: str, password: str
    ) -> "UserModel":
        validate_email(email)
        user: UserModel = self.model(
            email=email, first_name=first_name, last_name=last_name
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self, email: str, first_name: str, last_name: str, password: str
    ) -> None:
        validate_email(email)
        superuser = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name,
            is_superuser=True,
            is_verified=True,
            is_staff=True,
        )
        superuser.set_password(password)
        superuser.save(using=self._db)


class UserModel(base_user.AbstractBaseUser, auth_models.PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # type: ignore[var-annotated]
    first_name = models.CharField(max_length=255)  # type: ignore[var-annotated]
    last_name = models.CharField(max_length=255)  # type: ignore[var-annotated]
    email = models.EmailField(max_length=255, unique=True)  # type: ignore[var-annotated]
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)  # type: ignore[var-annotated]
    is_staff = models.BooleanField(default=False)  # type: ignore[var-annotated]
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)  # type: ignore[var-annotated]
    last_login = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"

    objects = _UserManager()

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def tokens(self) -> dict[str, str]:
        refresh = tokens.RefreshToken.for_user(self)
        access = tokens.AccessToken.for_user(self)
        return {
            "refresh": str(refresh),
            "access": str(access),
        }

    def to_entity(self) -> User:
        return User(
            id_=self.id,
            first_name=self.first_name,
            last_name=self.last_name,
            email=self.email,
            is_active=self.is_active,
            is_verified=self.is_verified,
            is_staff=self.is_staff,
            is_superuser=self.is_superuser,
            date_joined=self.date_joined,
            last_login=self.last_login,
        )
