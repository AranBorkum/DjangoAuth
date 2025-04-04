from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from django_auth.core.use_cases.logout_user import LogoutUser, LogoutUserOutputStatus
from django_auth.outputs import LogoutUserOutput
from django_auth.serializers import (
    LogoutUserSerializer,
)


class LogoutUserView(APIView):
    permission_classes = (IsAuthenticated,)
    _output_status_response_map = {
        LogoutUserOutputStatus.SUCCESS: status.HTTP_204_NO_CONTENT,
        LogoutUserOutputStatus.FAILED: status.HTTP_400_BAD_REQUEST,
    }

    def post(self, request: Request) -> Response:
        serializer = LogoutUserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        dto = serializer.to_dto()
        output = LogoutUserOutput()
        use_case = LogoutUser(output=output)
        use_case.logout(dto=dto)

        return Response(status=self._output_status_response_map[output.status])
