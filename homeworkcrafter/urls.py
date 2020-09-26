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
    path("review", views.review, name="review"),
    path("config/", views.stripe_config, name="stripeconfig"),
    path("create-checkout-session/", views.create_checkout_session, name="checkoutsession"),
    path("success/", views.paymentsuccess, name="paymentsuccess"),
    path("cancelled/", views.paymentcancelled, name="paymentcancelled"),
    #path("webhook", views.stripe_webhook, name="webhook")
]