import datetime

from django.contrib import messages
from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from talent_management_app.models import Goal
from talent_management_app.serializers import CreateGoalSerializer, ManagerGoalListSerializer


# Create your views here.
# def promote_employee(request):
# def onboard_employee(request):
# def employee_details(request):
# def schedule_training(request):
# def set_goals_for_employee(request):
# class RegisterTalent(APIView):
#     @staticmethod
#     def post(request):
#         serializer = RegisterTalentSerializer


class CreateGoalAPIView(CreateAPIView):
    queryset = Goal.objects.all()
    serializer_class = CreateGoalSerializer

    # def create(self, request,*args,**kwargs):
    #     serializer = self.serializer_class(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListGoalsAPIView(ListAPIView):
    serializer_class = ManagerGoalListSerializer

    def get_queryset(self):
        manager_id = self.kwargs['manager_id']
        return Goal.objects.filter(manager_id=manager_id)

