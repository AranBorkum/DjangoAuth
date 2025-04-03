from django.db.models import CASCADE, CharField, DateTimeField, Model, OneToOneField

from django_auth.core.entities import OneTimePassword
from django_auth.django_app.models._user import UserModel


class OneTimePasswordModel(Model):
    one_time_password = CharField(unique=True, max_length=6)
    user = OneToOneField(UserModel, on_delete=CASCADE)
    created_at = DateTimeField(auto_now_add=True)

    def to_entity(self) -> OneTimePassword:
        return OneTimePassword(
            one_time_password=self.one_time_password,
            user_id=self.user.id,
            created_at=self.created_at,
        )
