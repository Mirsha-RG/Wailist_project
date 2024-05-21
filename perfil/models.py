from django.db import models

from usuarios.models import User
# Create your models here.

class Perfil (models.Model):
    
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='user Id')
    nombre = models.CharField(max_length=128, null=True, verbose_name='empresa/usuario')
    descripcion = models.CharField( max_length=500, null=True, verbose_name='descripcion')
    contacto = models.CharField(max_length=128, null=True, verbose_name='contacto')
    redes = models.URLField(max_length=128, null=True, verbose_name='redes sociales')
    logo = models.ImageField(upload_to='perfil', default='default=jpg', verbose_name='logotipo')
    fecha = models,models.DateField(auto_now_add=True, verbose_name='fecha de creacion')
    status = models.BooleanField(default=True, verbose_name='estatus')
    
    class Meta:
        db_table = 'pefiles'
