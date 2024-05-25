from rest_framework import serializers
from .models import LandingPage

class LandingPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = LandingPage
        fields = '__all__'