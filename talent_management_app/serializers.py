from rest_framework import serializers

from talent_management_app.models import Training


class CreateTrainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Training
        fields = ['title', 'description', 'start_date', 'end_date', 'location', 'manager_email']
