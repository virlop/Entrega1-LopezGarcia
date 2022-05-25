from concurrent.futures.process import _MAX_WINDOWS_WORKERS
from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    altura = models.FloatField(default=0.0)

#MASCOTAS
class Mascota(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_adopcion = models.DateField()
    
    
class Perro(Mascota):
    raza = models.CharField(max_length=100)
    
    
class Gato(Mascota):
    color_pelaje = models.CharField(max_length=100)
    
