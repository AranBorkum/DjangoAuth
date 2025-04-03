from django_auth.core.use_cases.logout_user import LogoutUserDTO, LogoutUserPayload
from django_auth.django_app.serializers import LogoutUserSerializer


class TestLogoutUserSerializer:
    def test_serializer(self, logout_user_payload: LogoutUserPayload) -> None:
        assert LogoutUserSerializer(data=logout_user_payload).is_valid()

    def test_invalid_payload_serializer(
        self, logout_user_invalid_payload: LogoutUserPayload
    ) -> None:
        assert not LogoutUserSerializer(data=logout_user_invalid_payload).is_valid()

    def test_to_dto(self, logout_user_payload: LogoutUserPayload, token: str) -> None:
        serializer = LogoutUserSerializer(data=logout_user_payload)
        assert serializer.is_valid()
        dto = serializer.to_dto()
        assert isinstance(dto, LogoutUserDTO)
        assert dto.refresh_token == token
