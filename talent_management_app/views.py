from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from rest_framework.views import APIView
from talent_management_app.models import Talent, User, Skill
from talent_management_app.serializers import RegisterTalentSerializer, Promotion


# Create your views here.
# def promote_employee(request):
# def employee_details(request):
# def schedule_training(request):
# def set_goals_for_employee(request):
class RegisterTalent(APIView):
    @staticmethod
    def post(request):
        serializer = RegisterTalentSerializer
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


class PromoteEmployeeView(APIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = Promotion

    def post(self, request):
        user = request.user
        serializer = Promotion(data=request.data)
        serializer.is_valid(raise_exception=True)
        talent_id = request.data['talent_id']
        new_position = request.data['new_position']
        if user.role == 'MANAGER':
            talent = get_object_or_404(Talent, pk=talent_id)
            talent.position = new_position
            current_level_index = [level[0] for level in Talent.LEVEL_CHOICES].index(talent.level)
            if current_level_index < len(Talent.LEVEL_CHOICES) - 1:
                # talent.level = Talent.LEVEL_CHOICES[current_level_index + 1][0]
                Talent.objects.filter(id=talent_id).update(level=Talent.LEVEL_CHOICES[current_level_index + 1][0])
            return Response({'message': 'promoted'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Unauthorized'}, status=status.HTTP_400_BAD_REQUEST)
