from django.urls import path
from . import views

app_name="locations"
urlpatterns = [
    path("", views.showLocations.as_view(), name="list"),
    path("create/", views.createLocation, name="create"),
    path("detail/", views.getLocation, name="detail"),
    path("delete/", views.deleteLocation, name="delete"),
    path("get_states/", views.getStates, name="get_states"),
    path("get_cities/", views.getCities, name="get_cities"),
    path("get_actions/", views.actionsView, name="get_actions"),
]