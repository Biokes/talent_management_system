from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import CreateAPIView, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from talent_management_app.models import Training
from talent_management_app.serializers import CreateTrainingSerializer


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


class ScheduleTraining(CreateAPIView):
    queryset = Training.objects.all()
    serializer_class = CreateTrainingSerializer


class ScheduleTrainingList(APIView):
    def get(self, request):
        trainings = Training.objects.all()
        return Response(data=trainings, status=status.HTTP_200_OK)


class ViewTrainingForTrainner(APIView):
    def get(self, request):
        training = get_object_or_404(Training, training_id=request.data['training_id'])
        return Response(data=training, status=status.HTTP_200_OK)
