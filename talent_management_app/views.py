from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import CreateAPIView, get_object_or_404
from rest_framework.response import Response
from django.views.generic import CreateView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from talent_management_app.models import Training

from talent_management_app.models import Talent, User, Skill
from talent_management_app.serializers import RegisterTalentSerializer


# Create your views here.
# def promote_employee(request):
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
        serializer = RegisterTalentSerializer()
        if not serializer.is_valid:
            return Response(data={'message': 'INVALID DETAILS PROVIDED', 'success': False},
                            status=HTTP_400_BAD_REQUEST)
        email = serializer.data['email']
        password = serializer.data['password']
        phone_number = serializer.data['phone_number']
        user = User.objects.create(email=email, password=password,
                                   phone_number=phone_number, role='TALENT')
        talent = Talent.objects.create(user=user)
        Skill.objects.create(skill_name=serializer.data['skil_name'], proficiency=serializer.data['proficiency'],
                             talent_id=talent.pk)
        return Response(data={'messages': 'Registered successfully', 'success': True}
                        , status=HTTP_200_OK)
