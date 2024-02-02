from django.urls import path
from . import views

app_name = 'providers'
urlpatterns = [
    path("", views.showProviders.as_view(), name="list"),
    path("create/", views.createProvider, name="create"),
]