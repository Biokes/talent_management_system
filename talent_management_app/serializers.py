from rest_framework import serializers

from talent_management_app.models import Goal


class CreateGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = ['goal_name', 'goal_description', 'goal_category', 'target_date', 'goal_status',
                  ]


class ManagerGoalListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = ['id', 'goal_name', 'goal_description', 'goal_category', 'target_date', 'goal_status']
