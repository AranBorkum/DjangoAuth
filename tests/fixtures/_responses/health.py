from pytest import fixture
from rest_framework.response import Response
from rest_framework.test import APIClient


@fixture
def health_response() -> Response:
    return APIClient().get("/healthz/")
