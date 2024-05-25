from rest_framework import serializers
from captcha.fields import CaptchaField

from .models import Formulario

class FormularioSerializer(serializers.ModelSerializer):
    captcha = CaptchaField()
    
    class Meta:

        model = Formulario
        fields = ['usuario', 'email', 'phone', 'captcha']
        
    