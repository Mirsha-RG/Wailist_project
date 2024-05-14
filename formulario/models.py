from django.db import models

from listas.models import Lista
# Create your models here.
class Formulario(models.Model):
    
    lista = models.ForeignKey(Lista, on_delete=models.CASCADE, verbose_name='lista_id', null=True)
    usuario = models.CharField(max_length=120, verbose_name="Nombre usuario", null=True)
    email = models.EmailField(max_length=120, verbose_name= 'Correo Electronico', null=True)
    phone = models.CharField(max_length=120, verbose_name='telefono', null=True)
    company = models.CharField(max_length=120, verbose_name='empresa', null=False)
    created_date = models.DateField(auto_now_add=True, verbose_name='Fecha creación')
    status = models.BooleanField(default=True, verbose_name='Estatus')
    
    class Meta:
        db_table = 'formularios'

    