from pytest import fixture

from django_auth.django_app.views import LogoutUserView


@fixture
def logout_user_view() -> LogoutUserView:
    return LogoutUserView()
