# Generated by Django 4.0.1 on 2022-01-20 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0007_alter_empleado_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='empleado', verbose_name='Imagen'),
        ),
    ]
