from django.urls import path
from . import views

app_name="parameters"
urlpatterns = [
    path("", views.showParameters.as_view(), name="list"),
    path("create/", views.createParameter, name="create"),
    path("detail/", views.getParameter, name="detail"),
    path("delete/", views.deleteParameter, name="delete"),
]