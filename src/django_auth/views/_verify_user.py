from urllib.request import Request

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from django_auth.core.repository_interfaces import (
    OneTimePasswordRepositoryInterface,
    UserRepositoryInterface,
)
from django_auth.core.use_cases.verify_user import (
    VerifyUser,
    VerifyUserOutputType,
)
from django_auth.outputs import VerifyUserOutput
from django_auth.repositories import (
    OneTimePasswordRepository,
    UserRepository,
)
from django_auth.serializers import VerifyUserSerializer


class VerifyUserView(APIView):
    def __init__(
        self,
        user_repository: UserRepositoryInterface | None = None,
        otp_repository: OneTimePasswordRepositoryInterface | None = None,
    ) -> None:
        super().__init__()
        self._user_repository = user_repository or UserRepository()
        self._otp_repository = otp_repository or OneTimePasswordRepository()

        self._output_status_map: dict[VerifyUserOutputType, tuple[int, str]] = {
            VerifyUserOutputType.SUCCESS: (
                status.HTTP_200_OK,
                "User verified",
            ),
            VerifyUserOutputType.FAILURE: (
                status.HTTP_400_BAD_REQUEST,
                "User failed to verify",
            ),
        }

    def post(self, request: Request) -> Response:
        serializer = VerifyUserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        dto = serializer.to_dto()
        output = VerifyUserOutput()
        use_case = VerifyUser(
            user_repository=self._user_repository,
            otp_repository=self._otp_repository,
            output=output,
        )
        use_case.verify(dto=dto)
        response_status, response_message = self._output_status_map[output.status]
        return Response(response_message, status=response_status)
