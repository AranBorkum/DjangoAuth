import pytest
from django.utils import timezone

from django_auth.core import entities


@pytest.fixture
def verified_user_entity(
    email: str, password: str, first_name: str, last_name: str
) -> entities.User:
    return entities.User(
        email=email,
        first_name=first_name,
        last_name=last_name,
        is_active=True,
        is_verified=True,
        is_staff=False,
        is_superuser=False,
        date_joined=timezone.now(),
        last_login=timezone.now(),
    )
