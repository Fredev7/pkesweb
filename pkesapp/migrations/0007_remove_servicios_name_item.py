# Generated by Django 3.2.9 on 2021-12-01 20:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pkesapp', '0006_servicios_name_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicios',
            name='name_item',
        ),
    ]