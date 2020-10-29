from . import views
from django.urls import path, include


app_name = "main_api"

urlpatterns = [
    path('', views.api_overview, name="api_overview"),
    path('users/<str:user_query>', views.userdata, name="userdata"),
    path('topdecks/', views.topdecks, name="topdecks"),
    path('newdecks/', views.newdecks, name="newdecks"),
    path('search/<str:deck_query>/', views.search, name="search"),
    path('account/', views.new_account, name="new_account"),
    path('download/<str:pk>/', views.download, name="download"),
    path('upload/', views.upload, name="upload"),
    path('update/<str:pk>/', views.update, name="update"),
    path('delete/<str:user>&<str:deck_name>/', views.delete_deck, name="delete_deck"),
]
