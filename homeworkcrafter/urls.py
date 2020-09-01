from django.urls import path, include

app_name = "homeworkcrafter"
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("cotiza", views.fee, name="fee"),
    path("redeem", views.redeem, name="redeem"),
    path("express", views.express, name="express"),
    path("infohome", views.infohome, name="infohome"),
    path("infosecurity", views.infosecurity, name="infosecurity"),
    path("review", views.review, name="review")
]