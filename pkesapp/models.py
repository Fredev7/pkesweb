from django.db import models
from django.db.models.fields import CharField,TextField
from django.db.models.fields.files import ImageField


class Servicios(models.Model):
    name= CharField(max_length=30)
    descripcion= TextField()
    imagen= ImageField(upload_to="galeria", null=True)
    url_item=CharField(max_length=30)

    def __str__(self):
        return self.name



