# Generated by Django 4.1 on 2022-08-16 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0004_alter_empleado_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='imagen',
            field=models.ImageField(upload_to='static/images'),
        ),
    ]
