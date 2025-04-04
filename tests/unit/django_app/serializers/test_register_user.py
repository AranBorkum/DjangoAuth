from django_auth.core.use_cases.register_user import (
    RegisterUserDTO,
    RegisterUserPayload,
)
from django_auth.serializers import RegisterUserSerializer


class TestCaseRegisterUserSerializer:
    def test_serializer(self, register_user_payload: RegisterUserPayload) -> None:
        assert RegisterUserSerializer(data=register_user_payload).is_valid()

    def test_invalid_payload(
        self, register_user_invalid_payload: RegisterUserPayload
    ) -> None:
        assert not RegisterUserSerializer(data=register_user_invalid_payload).is_valid()

    def test_to_dto(self, register_user_payload: RegisterUserPayload) -> None:
        serializer = RegisterUserSerializer(data=register_user_payload)
        assert serializer.is_valid()
        dto = serializer.to_dto()
        assert isinstance(dto, RegisterUserDTO)
        assert dto.email == register_user_payload["email"]
        assert dto.password == register_user_payload["password"]
        assert dto.first_name == register_user_payload["first_name"]
        assert dto.last_name == register_user_payload["last_name"]
