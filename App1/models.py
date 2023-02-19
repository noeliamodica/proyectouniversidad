from django.db import models

# Create your models here.

class Estudiantes (models.Model):

    def __str__(self):
        return f"Nombre: {self.nombre} --- Carrera: {self.carrera}"


    nombre = models.CharField(max_length=50)
    carrera = models.CharField(max_length=30)

class Carreras (models.Model):

    def __str__(self):
        return f"Nombre: {self.nombre} --- Camada: {self.camada}"

    nombre = models.CharField(max_length=50)
    camada = models.IntegerField()

class Profesores (models.Model):

    def __str__(self):
        return f"Nombre: {self.nombre} --- Carrera: {self.carrera}"
    
    nombre = models.CharField(max_length=50)
    carrera = models.CharField(max_length=30)
    
