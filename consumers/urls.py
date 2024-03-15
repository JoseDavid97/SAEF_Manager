from django.urls import path
from . import views

app_name="consumers"
urlpatterns = [
    path("", views.showMeters.as_view(), name="list"),
    path("create/", views.createMeter, name="create"),
    path("detail/", views.getMeter, name="detail"),
    path("delete/", views.deleteMeter, name="delete"),
]