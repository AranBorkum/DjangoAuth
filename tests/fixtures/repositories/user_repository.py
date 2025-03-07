from collections.abc import Callable

import pytest

from django_auth.core import entities, repositories


@pytest.fixture
def user_repository(
    verified_user_entity: entities.User,
    email: str,
    full_name: str,
    access_token: str,
    refresh_token: str,
) -> Callable[[bool, bool], repositories.UserRepositoryInterface]:
    class FakeUserRepository(repositories.UserRepositoryInterface):  # type: ignore[misc]
        def __init__(
            self,
            *,
            get_user_by_email_success: bool = True,
            get_user_tokens_by_email_success: bool = True,
        ):
            self._get_user_by_email_success = get_user_by_email_success
            self._get_user_tokens_by_email_success = get_user_tokens_by_email_success

        def get_user_by_email(self, *, email: str) -> entities.User:
            if self._get_user_by_email_success:
                return verified_user_entity
            raise Exception("get_user_by_email failure")

        def get_user_tokens_by_email(self, *, email: str) -> dict[str, str]:
            if self._get_user_tokens_by_email_success:
                return dict(
                    access=access_token,
                    refresh=refresh_token,
                )
            raise Exception("get_user_tokens_by_email failure")

    def _factory(
        get_user_by_email: bool, get_user_tokens_by_email: bool
    ) -> FakeUserRepository:
        return FakeUserRepository(
            get_user_by_email_success=get_user_by_email,
            get_user_tokens_by_email_success=get_user_tokens_by_email,
        )

    return _factory
