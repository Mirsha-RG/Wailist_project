# Generated by Django 5.0.5 on 2024-05-10 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formulario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formulario',
            name='email',
            field=models.EmailField(max_length=120, null=True, verbose_name='Correo Electronico'),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='name_list',
            field=models.CharField(max_length=120, null=True, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='phone',
            field=models.CharField(max_length=120, null=True, verbose_name='telefono'),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='usuario',
            field=models.CharField(max_length=120, null=True, verbose_name='Nombre usuario'),
        ),
    ]