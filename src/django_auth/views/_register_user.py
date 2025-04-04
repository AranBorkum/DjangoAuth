from django.db.transaction import atomic
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from django_auth.core.repository_interfaces import (
    OneTimePasswordRepositoryInterface,
    UserRepositoryInterface,
)
from django_auth.core.use_cases.register_user import (
    RegisterUser,
    RegisterUserDTO,
    RegisterUserInterface,
    RegisterUserOutputType,
)
from django_auth.outputs import RegisterUserOutput
from django_auth.repositories import (
    OneTimePasswordRepository,
    UserRepository,
)
from django_auth.serializers import RegisterUserSerializer


class RegisterUserView(APIView):
    def __init__(
        self,
        user_repository: UserRepositoryInterface | None = None,
        otp_repository: OneTimePasswordRepositoryInterface | None = None,
    ):
        super().__init__()
        self._user_repository = user_repository
        self._otp_repository = otp_repository

        self._output_status_map: dict[RegisterUserOutputType, tuple[int, str]] = {
            RegisterUserOutputType.SUCCESS: (
                status.HTTP_201_CREATED,
                "User created",
            ),
            RegisterUserOutputType.FAILURE: (
                status.HTTP_400_BAD_REQUEST,
                "User registration failed",
            ),
        }

    @atomic
    def _register(self, use_case: RegisterUserInterface, dto: RegisterUserDTO) -> None:
        use_case.register(dto=dto)

    def post(self, request: Request) -> Response:
        serializer = RegisterUserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        dto = serializer.to_dto()
        user_repository = self._user_repository or UserRepository()
        otp_repository = self._otp_repository or OneTimePasswordRepository()
        output = RegisterUserOutput()
        use_case = RegisterUser(
            user_repository=user_repository,
            otp_repository=otp_repository,
            output=output,
        )
        self._register(use_case=use_case, dto=dto)
        response_status, response_message = self._output_status_map[output.status]
        return Response(response_message, status=response_status)
