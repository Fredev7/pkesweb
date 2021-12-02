from django.db import models
from django.db.models.fields import CharField,TextField
from django.db.models.fields.files import ImageField
# Create your models here.



class Galeria(models.Model):
    title= CharField(max_length=50)
    descripcion= TextField()
    imagen= ImageField(upload_to="galeria/galeria_app", null=True)
    created= models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title