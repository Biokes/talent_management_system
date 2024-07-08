from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import PROTECT

from talent_management_system import settings


# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=15)
    phone_number = models.CharField(max_length=250)
    ROLE_CHOICES = [('TALENT', 'Talent'), ('EMPLOYER', 'Employer'), ('MANAGER', 'Manager')]
    date_registered = models.DateTimeField(auto_now_add=True)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default='EMPLOYER')


class Employer(User):
    related_user_id = models.OneToOneField(User, on_delete=PROTECT, related_name="employer_user")


class Manager(User):
    user_id = models.OneToOneField(User, on_delete=PROTECT, related_name="manager_user")
    department_managed = models.CharField(max_length=255)


class Talent(User):
    user_id = models.OneToOneField(User, on_delete=PROTECT, related_name="talent_user")
    position = models.CharField(max_length=30)
    LEVEL = [('ONE', '1'), ('TWO', '2'), ('THREE', '3'), ('FOUR', '4'), ('FIVE', '5')]


class Skill(models.Model):
    talent_id = models.OneToOneField(Talent, on_delete=models.CASCADE, related_name="skill_user")
    skill_name = models.CharField(max_length=255)
    PROFICIENCY_LEVEL = [('B', 'BEGINNER'), ('I', 'INTERMEDIATE'), ('A', 'ADVANCED'), ('P', 'PROFESSIONAL')]
    proficiency = models.CharField(max_length=15, choices=PROFICIENCY_LEVEL, default='B')


# Create your models here.
# class User(AbstractUser):
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=15)
#     phone_number = models.CharField(max_length=15)
#

class Goal(models.Model):
    goal_id = models.AutoField(primary_key=True)
    goal_name = models.CharField(max_length=255)
    goal_description = models.CharField(max_length=255)
    target_date = models.DateTimeField(auto_now=True, blank=True, null=True)

    GOAL_STATUS = [
        ('O', 'OPEN'),
        ('P', 'PENDING'),
        ('I', 'IN_PROGRESS'),
        ('C', 'COMPLETED'),
    ]
    goal_status = models.CharField(max_length=255, choices=GOAL_STATUS, default='P')

    GOAL_CATEGORY = [
        ('F', 'FINANCE'),
        ('P', 'PERSONAL GOALS'),
        ('C', 'CAREER'),
        ('B', 'BUSINESS'),
        ('H', 'HEALTH'),

    ]
    goal_category = models.CharField(max_length=255, choices=GOAL_CATEGORY)
    manager_id = models.ForeignKey(Manager, on_delete=models.CASCADE)
