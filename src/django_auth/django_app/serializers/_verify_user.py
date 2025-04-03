from rest_framework.serializers import CharField, Serializer

from django_auth.core.use_cases.verify_user import VerifyUserDTO


class VerifyUserSerializer(Serializer):  # type: ignore[misc]
    one_time_password = CharField()

    def to_dto(self) -> VerifyUserDTO:
        return VerifyUserDTO(one_time_password=self.validated_data["one_time_password"])
