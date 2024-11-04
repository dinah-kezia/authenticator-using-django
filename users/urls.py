from django.urls import path
from .views import Register, LoginView, UserView, Logoutview


urlpatterns = [
    path("register/",Register.as_view(), name="register"),
    path("login/",LoginView.as_view(), name="login"),
    path("user/",UserView.as_view(), name="User View"),
    path("logout/",Logoutview.as_view(), name="logout"),
]
