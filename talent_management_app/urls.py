from django.urls import path

from talent_management_app import views

urlpatterns=[
    path('talent/register/',views.RegisterTalent.as_view()),
]
