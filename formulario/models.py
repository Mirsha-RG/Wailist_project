from django.db import models
from django import forms
from captcha.fields import CaptchaField

from listas.models import Lista
from usuarios.models import User
# Create your models here.
class Formulario(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='usuario id')
    lista = models.ForeignKey(Lista, on_delete=models.CASCADE, verbose_name='lista_id', null=True)
    usuario = models.CharField(max_length=120, verbose_name="Nombre usuario", null=True)
    email = models.EmailField(max_length=120, verbose_name= 'Correo Electronico', null=True)
    phone = models.CharField(max_length=120, verbose_name='telefono', null=True)
    company = models.CharField(max_length=120, verbose_name='empresa', null=False)
    created_date = models.DateField(auto_now_add=True, verbose_name='Fecha creación')
    status = models.BooleanField(default=True, verbose_name='Estatus')
    
    class Meta:
        db_table = 'formularios'
        
      
class FormularioForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Formulario
        fields = ['usuario', 'email', 'phone' ]  


    