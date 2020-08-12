from django.urls import path, include

app_name = "homeworkcrafter"
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("cotiza", views.fee, name="fee"),
    path("redeem", views.redeem, name="redeem")
]