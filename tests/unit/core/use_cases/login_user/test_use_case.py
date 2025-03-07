import pytest

from django_auth.core import use_cases
from django_auth.core.use_cases.login_user import dto


class TestLoginUserUseCase:
    def test_use_case(
        self,
        login_user_use_case: use_cases.LoginUser,
        login_user_dto: dto.LoginUserDTO,
        full_name: str,
        email: str,
        access_token: str,
        refresh_token: str,
    ) -> None:
        response_payload = login_user_use_case(login_dto=login_user_dto)
        assert response_payload["email"] == email
        assert response_payload["full_name"] == full_name
        assert response_payload["access_token"] == access_token
        assert response_payload["refresh_token"] == refresh_token

    def test_get_user_failed(
        self,
        login_user_get_user_failure_use_case: use_cases.LoginUser,
        login_user_dto: dto.LoginUserDTO,
    ) -> None:
        with pytest.raises(Exception) as exception:
            login_user_get_user_failure_use_case(login_dto=login_user_dto)

        assert exception.match("get_user_by_email failure")

    def test_get_tokens_failure(
        self,
        login_user_get_tokens_failure_use_case: use_cases.LoginUser,
        login_user_dto: dto.LoginUserDTO,
    ) -> None:
        with pytest.raises(Exception) as exception:
            login_user_get_tokens_failure_use_case(login_dto=login_user_dto)

        assert exception.match("get_user_tokens_by_email failure")
