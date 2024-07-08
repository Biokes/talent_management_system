from django.contrib.auth.models import AbstractUser
from django.db import models

from talent_management_system import settings


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
    goal_category = models.CharField(max_length=255,choices=GOAL_CATEGORY)
    # employeeId = models.ForeignKey(Employee, on_delete=models.CASCADE)
    # manager_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
