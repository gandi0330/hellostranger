from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')


    play1_title = models.CharField(max_length=20,  null=True)
    play1_rate = models.IntegerField(max_length=1,null=True)
    play2_title = models.CharField(max_length=20,  null=True)
    play2_rate = models.IntegerField(max_length=1,null=True)
    play3_title = models.CharField(max_length=20,  null=True)
    play3_rate = models.IntegerField(max_length=1, null=True)
