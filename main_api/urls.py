from . import views
from django.urls import path, include


app_name = "main_api"

urlpatterns = [
    path('', views.MainAPI, name="MainAPI"),
]
