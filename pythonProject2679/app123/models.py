from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Login(AbstractUser):
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)

class Task(models.Model):
    subject = models.CharField(max_length=25)
    description = models.TextField()

    def __str__(self):
        return self.subject


