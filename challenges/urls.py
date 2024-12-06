from django.urls import path

from . import views

urlpatterns = [

     path("", views.index),
    path("<int:month>", views.monthly_challenge_by_month),
    path("<str:month>", views.monthly_challenge, name = "month-challenge")
]
