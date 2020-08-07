from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

app_name = "welcome"
from . import views
urlpatterns = [
    path("", views.index, name = "index")
]
