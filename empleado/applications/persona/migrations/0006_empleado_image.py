# Generated by Django 4.0.1 on 2022-01-20 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0005_empleado_full_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='image',
            field=models.ImageField(default='imagen', upload_to=None, verbose_name='Imagen'),
        ),
    ]
