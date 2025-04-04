from pytest import fixture
from rest_framework.response import Response
from rest_framework.test import APIClient

from django_auth.core.use_cases.verify_user import VerifyUserPayload
from django_auth.models import OneTimePasswordModel, UserModel


@fixture
def verify_user_response(
    verify_user_payload: VerifyUserPayload,
    unverified_user_model: UserModel,
    one_time_password_model: OneTimePasswordModel,
) -> Response:
    return APIClient().post("/auth/verify/", verify_user_payload)


@fixture
def verify_user_invalid_payload_response(
    verify_user_invalid_payload: VerifyUserPayload,
    unverified_user_model: UserModel,
    one_time_password_model: OneTimePasswordModel,
) -> Response:
    return APIClient().post("/auth/verify/", verify_user_invalid_payload)


@fixture
def verify_user_already_verified_response(
    verify_user_payload: VerifyUserPayload,
    verified_user_model: UserModel,
    one_time_password_verified_user_model: OneTimePasswordModel,
) -> Response:
    return APIClient().post("/auth/verify/", verify_user_payload)
