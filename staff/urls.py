from django.urls import path, include

from . import views


app_name = "staff"
urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("<int:homework_id>", views.homework, name="homework"),
    path("addjob", views.addjob, name="addjob")
]