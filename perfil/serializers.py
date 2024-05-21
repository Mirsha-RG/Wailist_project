from rest_framework import serializers

from .models import Perfil

class PerfilSerializer(serializers.ModelSerializer):
    is_active = serializers.BooleanField(required=False)
    
    class Meta:
        model = Perfil
        fields = '__all__'