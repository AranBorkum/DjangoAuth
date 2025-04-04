from pytest import fixture

from django_auth.views import LogoutUserView


@fixture
def logout_user_view() -> LogoutUserView:
    return LogoutUserView()
