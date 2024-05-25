from django.db import models

from usuarios.models import User
# Create your models here.

class LandingPage (models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='user_id')
    empresa = models.CharField(max_length=128, verbose_name='nombre empresa',null=True )
    descripcion = models.CharField(max_length=600, verbose_name='descripcion',null=True )
    contacto = models.CharField(max_length=128, verbose_name='contacto',null=True )
    redes = models.URLField(max_length=128, verbose_name='url',null=True )   
    logo = models.ImageField(upload_to='imagen', default='default=jpg', verbose_name='logotipo') 
    is_private = models.BooleanField(default=False, verbose_name='privada/publica')
    date = models.DateTimeField(auto_now_add=True, verbose_name='fecha de creacion')
    status = models.BooleanField(default=True, verbose_name='status')
    
    class Meta:
        db_table = 'paginas_web'