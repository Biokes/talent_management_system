from rest_framework import serializers

from talent_management_app.models import Talent


class RegisterTalentSerializer(serializers.Serializer):
    class Meta:
        model = Talent
        fields = ['first_name', 'last_name', 'email','password','phone_number','role','skill_name','proficiency']