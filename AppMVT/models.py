from statistics import mode
from django.db import models


# Create your models here.

class Familia(models.Model):

    nombre = models.CharField(max_length=60)
    edad = models.IntegerField()
    pais = models.CharField(max_length=60)