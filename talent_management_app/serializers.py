from rest_framework import serializers

from talent_management_app.models import Goal
from talent_management_app.models import Talent


class CreateGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = ['goal_name', 'goal_description', 'goal_category', 'target_date', 'goal_status',
                  ]


class ManagerGoalListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = ['manager_id','id', 'goal_name', 'goal_description', 'goal_category', 'target_date', 'goal_status']


class RegisterTalentSerializer(serializers.Serializer):
    class Meta:
        model = Talent
        fields = ['email', 'password', 'phone_number', 'skill_name', 'proficiency']
