from django.db import models

# Create your models here.

class Play(models.Model):
    title = models.CharField(max_length=200, null=True)
    ganre = models.TextField(null=True)