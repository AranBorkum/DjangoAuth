from pytest import fixture

from django_auth.core.use_cases.verify_user import VerifyUserPayload


@fixture
def verify_user_payload(one_time_password: str) -> VerifyUserPayload:
    return VerifyUserPayload(
        one_time_password=one_time_password,
    )


@fixture
def verify_user_invalid_payload(one_time_password: str) -> VerifyUserPayload:
    return VerifyUserPayload(one_time_password="")
