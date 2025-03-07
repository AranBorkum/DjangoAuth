from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from django_auth.django_app import views

urlpatterns = [
    path("login/", views.LoginUserView.as_view(), name="login"),
    path("refresh/", jwt_views.TokenRefreshView.as_view(), name="refresh"),
]
