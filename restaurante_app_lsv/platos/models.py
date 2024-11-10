from django.db import models

# Create your models here.
class platos(models.Model):
    Nombre = models.CharField(max_length=20)
    Precio = models.IntegerField(default=0)
