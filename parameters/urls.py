from django.urls import path
from . import views

app_name="parameters"
urlpatterns = [
    path("", views.showParameters, name="list"),
]