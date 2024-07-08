from django.shortcuts import render
from rest_framework.views import APIView

from talent_management_app.serializers import RegisterTalentSerializer


# Create your views here.
# def promote_employee(request):
# def onboard_employee(request):
# def employee_details(request):
# def schedule_training(request):
# def set_goals_for_employee(request):
class RegisterTalent(APIView):
    @staticmethod
    def post(request):
        serializer = RegisterTalentSerializer
