import datetime

from django.contrib import messages
from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from talent_management_app.models import Goal
from talent_management_app.serializers import CreateGoalSerializer, ManagerGoalListSerializer

from django.shortcuts import render
from django.views.generic import CreateView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from rest_framework.views import APIView

from talent_management_app.models import Talent, User, Skill

from talent_management_app.serializers import RegisterTalentSerializer


class CreateGoalAPIView(CreateAPIView):
    queryset = Goal.objects.all()
    serializer_class = CreateGoalSerializer


class ListGoalsAPIView(ListAPIView):
    serializer_class = ManagerGoalListSerializer

    def get_queryset(self):
        serializer = ManagerGoalListSerializer()
        if not serializer.is_valid():
            return Response(data={"invalid "}, status=status.HTTP_400_BAD_REQUEST)

        manager_id = self.kwargs['manager_id']
        return Goal.objects.filter(manager_id=manager_id)


class RegisterTalent(APIView):
    @staticmethod
    def post(request):
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
