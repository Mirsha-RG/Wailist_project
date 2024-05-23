from django.db import models

from formulario.models import Formulario
from listas.models import Lista

# Create your models here.

class VisitasFormulario(models.Model):
    Formulario = models.ForeignKey(Formulario, on_delete=models.CASCADE, verbose_name='visitas formulario', null=True)
    ip = models.GenericIPAddressField( max_length=50, null=True, verbose_name='ip usuario')
    browser = models.CharField( max_length=50, null=True, verbose_name='navegador')
    os = models.CharField( max_length=50, null=True, verbose_name='sistema  operativo')
    device = models.CharField(max_length=50, verbose_name='dispositivo')
    country = models.CharField(max_length=50, null=True, verbose_name='pais') 
    city = models.CharField(max_length=50, null=True, verbose_name='ciudad')
    path = models.CharField(max_length=250, null=True, verbose_name='ruta url')
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'Formulario_visitas'
        
        
class VisitasLista(models.Model):
    lista = models.ForeignKey(Formulario, on_delete=models.CASCADE, verbose_name='visitas formulario', null=True)
    ip = models.GenericIPAddressField( max_length=50, null=True, verbose_name='ip usuario')
    browser = models.CharField( max_length=50, null=True, verbose_name='navegador')
    os = models.CharField( max_length=50, null=True, verbose_name='sistema  operativo')
    device = models.CharField(max_length=50, verbose_name='dispositivo')
    country = models.CharField(max_length=50, null=True, verbose_name='pais') 
    city = models.CharField(max_length=50, null=True, verbose_name='ciudad')
    path = models.CharField(max_length=250, null=True, verbose_name='ruta url')
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'Lista_visitas'
    
    
                              
