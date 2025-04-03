from django_auth.core.use_cases.verify_user import VerifyUserDTO, VerifyUserPayload
from django_auth.django_app.serializers import VerifyUserSerializer


class TestCaseVerifyUserSerializer:
    def test_serializer(self, verify_user_payload: VerifyUserPayload) -> None:
        assert VerifyUserSerializer(data=verify_user_payload).is_valid()

    def test_invalid_payload(
        self, verify_user_invalid_payload: VerifyUserPayload
    ) -> None:
        assert not VerifyUserSerializer(data=verify_user_invalid_payload).is_valid()

    def test_to_dto(self, verify_user_payload: VerifyUserPayload) -> None:
        serializer = VerifyUserSerializer(data=verify_user_payload)
        assert serializer.is_valid()
        dto = serializer.to_dto()
        assert isinstance(dto, VerifyUserDTO)
        assert dto.one_time_password == verify_user_payload["one_time_password"]
