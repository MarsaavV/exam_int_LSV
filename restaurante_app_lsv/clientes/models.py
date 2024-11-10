from django.db import models

# Create your models here.
class Clientes (models.Model):
    Nombre = models.CharField(max_length=20)
    Apellido = models.CharField(max_length=20)
    DNI = models.CharField(max_length=8, default='00000000')
