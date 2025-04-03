from django_auth.core.entities import User
from django_auth.core.repository_interfaces import UserRepositoryInterface
from django_auth.core.use_cases.get_user._dto import GetUserDTO
from django_auth.core.use_cases.get_user._interface import GetUserInterface
from django_auth.core.use_cases.get_user._output import GetUserOutputInterface


class GetUser(GetUserInterface):  # type: ignore
    def __init__(
        self, repository: UserRepositoryInterface, output: GetUserOutputInterface
    ) -> None:
        self._repository = repository
        self._output = output

    def retrieve(self, dto: GetUserDTO) -> None:
        user: User = self._repository.get_user_by_user_id(user_id=dto.user_id)
        self._output.finalize(user=user)
