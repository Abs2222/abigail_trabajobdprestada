# Generated by Django 4.1 on 2022-08-16 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0002_empleado_delete_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='imagen',
            field=models.ImageField(upload_to='static/'),
        ),
    ]