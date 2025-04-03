from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from django_auth.core.use_cases.login_user import LoginUser
from django_auth.django_app.outputs import LoginUserOutput
from django_auth.django_app.serializers import LoginUserSerializer


class LoginUserView(APIView):  # type: ignore[misc]
    def post(self, request: Request) -> Response:
        serializer = LoginUserSerializer(
            authenticator=authenticate,
            data=request.data,
            context={"request": request},
        )

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        dto = serializer.to_dto()
        output = LoginUserOutput()
        use_case = LoginUser(output=output)
        use_case.login(dto=dto)
        return Response(output.login_token_response, status=status.HTTP_200_OK)
