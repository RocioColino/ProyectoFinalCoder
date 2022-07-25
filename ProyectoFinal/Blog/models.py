from django.db import models
from django.contrib.auth.models import User
from django.forms import CharField, ImageField
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField


class Categoria(models.Model):
    nombre=models.CharField(max_length=255)

    def __str__(self):
           return self.nombre 

    def get_absolute_url(self):
        return reverse('blog')


class Post(models.Model):
   titulo=models.CharField(max_length=255)
   subtitulo=models.CharField(max_length=200)
   autor=models.ForeignKey(User, on_delete=models.CASCADE)
   fecha=models.DateField(auto_now_add=True)
   imagen=models.ImageField(null=True, blank=True, upload_to="images/")
   cuerpo=RichTextField(blank=True, null=True)
   #cuerpo=models.TextField()
   categoria=models.CharField(max_length=255, default='Turismo')
   fragmento=models.CharField(max_length=150)

   def __str__(self):
       return self.titulo + '︱' + str(self.autor) + '︱' + str(self.fecha)

   def get_absolute_url(self):
        return reverse('blog')


class Lugares(models.Model):
    nombre=models.CharField(max_length=250)
    imagen=models.ImageField()
    descripcion=models.TextField()
    direccion=models.CharField(max_length=50)
    contacto=models.CharField(max_length=100)

    def __str__(self):
        return self.nombre + '︱' + self.contacto

