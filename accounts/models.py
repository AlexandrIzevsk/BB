from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class OneCode(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='code_user')
    code = models.CharField(max_length=5)
