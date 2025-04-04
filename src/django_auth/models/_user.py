from uuid import uuid4

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import validate_email
from django.db.models import (
    BooleanField,
    CharField,
    DateTimeField,
    EmailField,
    UUIDField,
)
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken

from django_auth.core.entities import User


class UserModel(AbstractBaseUser, PermissionsMixin):
    class UserManager(BaseUserManager):
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

    id = UUIDField(primary_key=True, default=uuid4, editable=False)
    first_name = CharField(max_length=255)
    last_name = CharField(max_length=255)
    email = EmailField(max_length=255, unique=True)

    is_active = BooleanField(default=True)
    is_verified = BooleanField(default=False)
    is_staff = BooleanField(default=False)
    is_superuser = BooleanField(default=False)

    date_joined = DateTimeField(auto_now_add=True)
    last_login = DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"

    objects = UserManager()

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def tokens(self) -> dict[str, str]:
        refresh = RefreshToken.for_user(self)
        access = AccessToken.for_user(self)
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
