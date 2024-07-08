from django.urls import path

from talent_management_app import views
from talent_management_app.views import ListGoalsAPIView

urlpatterns = [

    path("create_goal/", views.CreateGoalAPIView.as_view()),
    path('managers/<int:manager_id>/goals/', views.ListGoalsAPIView.as_view(), name='list_goals')
]