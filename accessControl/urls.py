from django.urls import path
from . import views

app_name="accessControl"
urlpatterns = [
    path("", views.home, name="home"),
    path("accounts/login/", views.loginView, name="login"),
]