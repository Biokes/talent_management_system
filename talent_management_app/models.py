from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import PROTECT


# Create your models here.
class User(AbstractUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=15)
    phone_number = models.CharField(max_length=15)
    ROLE_CHOICES = [('TALENT', 'Talent'), ('EMPLOYER', 'Employer')]
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default='EMPLOYER')
class Employer(User):
    user= models.OneToOneField(User,on_delete=PROTECT)
    date_joined = models.DateTimeField(auto_now_add=True)

class Talent(User):
    user= models.OneToOneField(User,on_delete=PROTECT)


class Skill(models.Model):
    talent_id = models.OneToOneField(Talent, on_delete=models.CASCADE, null=True, blank=True)
    skill_name = models.CharField(max_length=255)
    PROFICIENCY_LEVEL = [('B', 'BEGINNER'), ('I', 'INTERMEDIATE'), ('A', 'ADVANCED'), ('P', 'PROFESSIONAL')]
    proficiency = models.CharField(max_length=15, choices=PROFICIENCY_LEVEL, default='B')
