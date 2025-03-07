from django.contrib.auth import authenticate
from rest_framework import request, response, status, views

from django_auth.core import use_cases
from django_auth.django_app import repositories, serializers


class LoginUserView(views.APIView):  # type: ignore[misc]
    def post(self, request: request.Request) -> response.Response:
        serializer = serializers.LoginUserSerializer(
            authenticator=authenticate,
            data=request.data,
            context={"request": request},
        )

        if not serializer.is_valid():
            return response.Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

        dto = serializer.to_dto()
        user_repository = repositories.UserRepository()
        login_user = use_cases.LoginUser(repository=user_repository)
        response_payload = login_user(login_dto=dto)
        return response.Response(response_payload, status=status.HTTP_200_OK)
