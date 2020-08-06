from django.urls import path, include

from django.contrib import admin

admin.autodiscover()


from . import views
urlpatterns = [
    path("", welcome.views.index, name = "index")
]
