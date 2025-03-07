import pytest

from django_auth.django_app import views


@pytest.fixture
def login_user_view() -> views.LoginUserView:
    return views.LoginUserView()
