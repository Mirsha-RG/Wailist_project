from rest_framework import serializers

from formulario.serializers import FormularioSerializer
from .models import Lista

class ListaSerializer(serializers.ModelSerializer):
    is_active = serializers.BooleanField(required=False)  # Campo para manejar la opción de privacidad

    class Meta:
        model = Lista
        fields = '__all__'
        
class ListListaSerializer(serializers.ModelSerializer):
    is_active = serializers.BooleanField(required=False)  

    class Meta:
        model = Lista
        fields = '__all__'
    
    def to_representation(self, instance):
                response = super().to_representation(self,instance)
                response['Formulario'] = FormularioSerializer(instance.empresa).data
                return response