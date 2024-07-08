from django.urls import path

from talent_management_app import views
from talent_management_app.views import ScheduleTrainingList, ViewTrainingForTrainner

urlpatterns = [
    path('schedule_training', views.ScheduleTraining.as_view(), name='schedule_training'),
    path('view_trainings', ScheduleTrainingList.as_view(), name='view_trainings'),
    path('view_training/<str:training_id>', ViewTrainingForTrainner.as_view(), name='view_training'),
    path('talent/register/',views.RegisterTalent.as_view()),
    path("create_goal/", views.CreateGoalAPIView.as_view()),
    path('managers/<int:manager_id>/goals/', views.ListGoalsAPIView.as_view(), name='list_goals')
]
