from django.db import transaction
from django.shortcuts import render
from django.views.generic import CreateView
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from rest_framework.views import APIView

<<<<<<< HEAD
=======
from talent_management_app.models import Talent, User, Skill
<<<<<<< HEAD
>>>>>>> Abbey
from talent_management_app.serializers import RegisterTalentSerializer
=======
from talent_management_app.serializers import RegisterTalentSerializer, ViewTalentProfileSerializer
>>>>>>> Abbey


# Create your views here.
# def promote_employee(request):
# def employee_details(request):
# def schedule_training(request):
# def set_goals_for_employee(request):
class RegisterTalent(APIView):
    @staticmethod
    @transaction.atomic
    def post(request):
<<<<<<< HEAD
        serializer = RegisterTalentSerializer
=======
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
<<<<<<< HEAD
        return Response(data={'messages': 'Registered successfully', 'success': True}
                        , status=HTTP_200_OK)
>>>>>>> Abbey
=======
        return Response({'messages': 'Registered successfully', 'success': True},status=HTTP_200_OK)

    @staticmethod
    def get(request):
        serializer= ViewTalentProfileSerializer()
        if not serializer.is_valid:
            return Response({'message': 'INVALID DETAILS PROVIDED', 'success': False},
                            status=HTTP_400_BAD_REQUEST)
        talent = get_object_or_404(pk=serializer.data['email'])
        phone_number = talent.phone_number
        email= talent.email
        skill = Skill.objects.filter(pk=User.objects.filter(email)).get().proficiency
        return Response({"skill_level":f"{skill}","talent":f"{phone_number}",})

>>>>>>> Abbey
