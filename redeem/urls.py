from django.urls import path, include



from . import views

app_name = "redeem"
urlpatterns = [
    path("", views.index, name="index")
]