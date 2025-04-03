from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from django_auth.django_app.views import (
    GetUserView,
    LoginUserView,
    LogoutUserView,
    RegisterUserView,
    VerifyUserView,
)

urlpatterns = [
    path("register/", RegisterUserView.as_view(), name="register"),
    path("verify/", VerifyUserView.as_view(), name="verify"),
    path("login/", LoginUserView.as_view(), name="login"),
    path("logout/", LogoutUserView.as_view(), name="logout"),
    path("refresh/", TokenRefreshView.as_view(), name="refresh"),
    path("me/", GetUserView.as_view(), name="me"),
]
