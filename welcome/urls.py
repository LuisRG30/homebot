from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

app_name = "welcome"
import welcome.views
urlpatterns = [
    path("", views.index, name = "index")
]
