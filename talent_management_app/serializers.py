from rest_framework import serializers

from talent_management_app.models import Talent


class RegisterTalentSerializer(serializers.Serializer):
    class Meta:
        model = Talent
        fields = ['email','password','phone_number','skill_name','proficiency']