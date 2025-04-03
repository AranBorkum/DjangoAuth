from rest_framework.serializers import CharField, EmailField, Serializer

from django_auth.core.use_cases.register_user import RegisterUserDTO


class RegisterUserSerializer(Serializer):  # type: ignore[misc]
    email = EmailField()
    password = CharField(write_only=True)
    first_name = CharField()
    last_name = CharField()

    def to_dto(self) -> RegisterUserDTO:
        return RegisterUserDTO(
            email=self.validated_data["email"],
            password=self.validated_data["password"],
            first_name=self.validated_data["first_name"],
            last_name=self.validated_data["last_name"],
        )
