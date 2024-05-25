from django.db import models

from usuarios.models import User
# Create your models here.
class Lista (models.Model):
    
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='usuario id')
    name = models.CharField(max_length=120, verbose_name="Nombre lista", null=True)
    descrption = models.CharField(max_length=400, verbose_name= 'descripcion', null=True)
    message = models.CharField(max_length=400, verbose_name= 'mensaje de correo', null=True)
    url = models.URLField(max_length=200, verbose_name='url personalizada', null=True)
    is_active = models.BooleanField(default=True, verbose_name='activa/pausa') 
    created_date = models.DateField(auto_now_add=True, verbose_name='Fecha creación')
    status = models.BooleanField(default=True, verbose_name='Estatus')
    
    class Meta:
        db_table = 'listas'
      
    
    
    