from django.db import models

# Create your models here.

class Play(models.Model):
    title = models.CharField(max_length=200, null=True)
    # image = models.ImageField(upload_to='producer/', null=True)
    genres = models.CharField(max_length=200, null=True)
    area = models.CharField(max_length=200, null=True)
    rate =models.CharField(max_length=2,null=True)
    vote = models.CharField(max_length=10,null=True)

