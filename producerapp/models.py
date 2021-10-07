from django.db import models

# Create your models here.

class Play(models.Model):
    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='producer/', null=True)
    genre = models.CharField(max_length=200, null=True)
    location = models.CharField(max_length=200, null=True)
    etc = models.TextField(null=True)