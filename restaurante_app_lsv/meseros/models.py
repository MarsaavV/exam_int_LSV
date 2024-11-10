from django.db import models

# Create your models here.
class meseros(models.Model):
    Nombre = models.CharField(max_length=20)
    Nacionalidad = models.CharField(max_length=20)
    Edad = models.IntegerField(default=0)