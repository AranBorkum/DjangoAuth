from django_auth.core.use_cases.register_user import (
    RegisterUserDTO,
    RegisterUserInterface,
    RegisterUserOutputInterface,
    RegisterUserOutputType,
)


class TestCaseRegisterUser:
    def test_register_new_user(
        self,
        register_user_use_case: RegisterUserInterface,
        register_user_dto: RegisterUserDTO,
        register_user_output: RegisterUserOutputInterface,
    ) -> None:
        register_user_use_case.register(dto=register_user_dto)
        assert register_user_output.status == RegisterUserOutputType.SUCCESS

    def test_register_existing_user(
        self,
        register_user_already_exists_use_case: RegisterUserInterface,
        register_user_dto: RegisterUserDTO,
        register_user_output: RegisterUserOutputInterface,
    ) -> None:
        register_user_already_exists_use_case.register(dto=register_user_dto)
        assert register_user_output.status == RegisterUserOutputType.FAILURE
