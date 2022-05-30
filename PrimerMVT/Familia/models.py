from django.db import models

# Create your models here.
class Familiares(models.Model):
    nombre=models.CharField(max_length=30)
    edad=models.IntegerField()
    parentesco=models.CharField(max_length=40)
    email=models.EmailField()
    telefono=models.CharField(max_length=10)
    f_nacimiento=models.DateField(blank=True,null=True)

    def __str__ (self):
        return self.nombre

class Sobre_mi(models.Model):
    nombre=models.CharField(max_length=30)
    edad=models.IntegerField()
    email=models.EmailField()
    telefono=models.CharField(max_length=10)
    f_nacimiento=models.DateField(blank=True,null=True)

    def __str__ (self):
        return self.nombre
