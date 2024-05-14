from django.db import models

# Create your models here.
class Lista (models.Model):
    
    name = models.CharField(max_length=120, verbose_name="Nombre lista", null=True)
    descrption = models.CharField(max_length=400, verbose_name= 'descripcion', null=True)
    is_active = models.BooleanField(default=True, verbose_name='activa/pausa') 
    created_date = models.DateField(auto_now_add=True, verbose_name='Fecha creación')
    status = models.BooleanField(default=True, verbose_name='Estatus')
    
    class Meta:
        db_table = 'listas'
      
    
    
    