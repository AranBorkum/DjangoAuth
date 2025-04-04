from rest_framework.serializers import CharField, Serializer

from django_auth.core.use_cases.logout_user import LogoutUserDTO


class LogoutUserSerializer(Serializer):
    refresh_token = CharField()

    def to_dto(self) -> LogoutUserDTO:
        return LogoutUserDTO(refresh_token=self.validated_data["refresh_token"])
