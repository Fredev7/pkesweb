from django.db import models
from django.db.models.fields import CharField, TextField
from django.db.models.fields.files import ImageField


class Services(models.Model):
    name = CharField(max_length=30)
    description = TextField()
    image = ImageField(upload_to="gallery/sevices_app", null=True)
    url_item = CharField(max_length=30)

    def __str__(self):
        return self.name
