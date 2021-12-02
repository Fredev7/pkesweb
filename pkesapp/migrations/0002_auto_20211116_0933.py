# Generated by Django 3.2.9 on 2021-11-16 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pkesapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='galeria',
            name='descripcion',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='galeria',
            name='imagen',
            field=models.ImageField(default='', upload_to='galeria'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='galeria',
            name='name',
            field=models.CharField(default='Galeria', max_length=30),
            preserve_default=False,
        ),
    ]
