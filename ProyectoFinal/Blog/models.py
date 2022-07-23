from django.db import models
from django.contrib.auth.models import User
from django.forms import CharField, ImageField

class Post(models.Model):
   titulo=models.CharField(max_length=255)
   subtitulo=models.CharField(max_length=200)
   autor=models.ForeignKey(User, on_delete=models.CASCADE)
   fecha=models.DateField()
   imagen=models.ImageField()
   cuerpo=models.TextField()

   def __str__(self):
       return self.titulo + '︱' + str(self.autor) + '︱' + str(self.fecha)

class Lugares(models.Model):
    nombre=models.CharField(max_length=250)
    imagen=models.ImageField()
    descripcion=models.TextField()
    direccion=models.CharField(max_length=50)
    contacto=models.CharField(max_length=100)

    def __str__(self):
        return self.nombre + '︱' + self.contacto

