from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import PROTECT


# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=15)
    phone_number = models.CharField(max_length=250)
    ROLE_CHOICES = [('TALENT', 'Talent'), ('EMPLOYER', 'Employer')]
    date_registered = models.DateTimeField(auto_now_add=True)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default='EMPLOYER')


class Employer(User):
    related_user_id = models.OneToOneField(User, on_delete=PROTECT, related_name="employer_user")


class Manager(User):
    user_id = models.OneToOneField(User, on_delete=PROTECT, related_name="manager_user")
    department_managed = models.CharField(max_length=255)


class Talent(User):
    user_id = models.OneToOneField(User, on_delete=PROTECT, related_name="talent_user")


class Skill(models.Model):
    talent_id = models.OneToOneField(Talent, on_delete=models.CASCADE, related_name="skill_user")
    skill_name = models.CharField(max_length=255)
    PROFICIENCY_LEVEL = [('B', 'BEGINNER'), ('I', 'INTERMEDIATE'), ('A', 'ADVANCED'), ('P', 'PROFESSIONAL')]
    proficiency = models.CharField(max_length=15, choices=PROFICIENCY_LEVEL, default='B')


class Training(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    location = models.CharField(max_length=255)
    manager_email = models.EmailField(default="no email")
