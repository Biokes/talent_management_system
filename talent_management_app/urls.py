from django.urls import path

from talent_management_app import views
from talent_management_app.views import PromoteEmployeeView

urlpatterns = [
    path('talent/register/', views.RegisterTalent.as_view()),
    path('talent/promote/', PromoteEmployeeView.as_view()),
]
