from django.urls import path
from users.views import UserListView, LoginView, RegisterView


urlpatterns = [
    path("", UserListView.as_view(), name="home"),
    path("user/login/", LoginView.as_view(), name="login-view"),
    path("user/register/", RegisterView.as_view(), name="register-view")
]