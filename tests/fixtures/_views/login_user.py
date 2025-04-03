from pytest import fixture

from django_auth.django_app.views import LoginUserView


@fixture
def login_user_view() -> LoginUserView:
    return LoginUserView()
