from uuid import UUID

from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from django_auth.core.use_cases.get_user import GetUser, GetUserDTO
from django_auth.outputs import GetUserOutput
from django_auth.repositories import UserRepository


class GetUserView(APIView):
    def get(self, request: Request) -> Response:
        user_id: UUID | None = request.user.id
        if user_id is None:
            return Response(status=status.HTTP_204_NO_CONTENT)

        dto = GetUserDTO(user_id=user_id)
        output = GetUserOutput()
        repository = UserRepository()
        use_case = GetUser(repository=repository, output=output)
        use_case.retrieve(dto=dto)
        return Response(output.user, status=status.HTTP_200_OK)
