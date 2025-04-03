from pytest import fixture

from django_auth.core.use_cases.register_user import RegisterUserDTO


@fixture
def register_user_dto(
    email: str, password: str, first_name: str, last_name: str
) -> RegisterUserDTO:
    return RegisterUserDTO(
        email=email,
        password=password,
        first_name=first_name,
        last_name=last_name,
    )
