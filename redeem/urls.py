from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

app_name = "redeem"
from . import views
urlpatterns = [
    path("", views.index, name = "indexredeem")
]