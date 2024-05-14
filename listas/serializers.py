from rest_framework import serializers

from .models import Lista

class ListaSerializer(serializers.ModelSerializer):
    is_active = serializers.BooleanField(required=False)  # Campo para manejar la opción de privacidad

    class Meta:
        model = Lista
        fields = '__all__'