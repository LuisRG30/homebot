from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

app_name = "redeem"
import redeem.views