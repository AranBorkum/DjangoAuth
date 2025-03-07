import pytest

from django_auth.core.use_cases.login_user import dto


@pytest.fixture
def login_user_dto(email: str, password: str) -> dto.LoginUserDTO:
    return dto.LoginUserDTO(
        email=email,
        password=password,
    )
