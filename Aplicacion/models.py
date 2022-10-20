
from django.db import models

# Create your models here.
class Doctor(models.Model):
    nombres=models.CharField(max_length=50)
    apellidos=models.CharField(max_length=50)
    numColMed=models.PositiveSmallIntegerField()
    especialidad=models.CharField(max_length=50)
    celular=models.PositiveSmallIntegerField()
    email=models.EmailField()

class Paciente(models.Model):
    nombres=models.CharField(max_length=50)
    apellidos=models.CharField(max_length=50)
    DNI=models.PositiveSmallIntegerField()
    edad=models.PositiveSmallIntegerField()
    numHistoria=models.PositiveSmallIntegerField()
    celular=models.PositiveSmallIntegerField()
    direccion=models.CharField(max_length=50)
