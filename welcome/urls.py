from django.urls import path, include

app_name = "welcome"
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("cotiza", views.fee, name="fee")
]