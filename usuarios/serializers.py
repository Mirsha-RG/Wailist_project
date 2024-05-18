from django.contrib.auth import get_user_model, authenticate

from rest_framework import serializers

from .models import User

class RegisterUserSerializer(serializers.ModelSerializer):

   class Meta:
        model = get_user_model()
        fields = [ 'first_name', 'last_name', 'company', 'email', 'password']
        extra_kwargs = {'password':{'write_only': True}}
    
   def create(self, validated_data):
       return get_user_model().objects.create_user(**validated_data)
        
   def update(self,instance, validated_data):
       password = validated_data.pop('password', None)
       user = super().update(instance, validated_data)
       
       if password:
           user.set_password(password)
           user.save()
           
       return user
   


class AuthTokenSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(style={'input_type': 'password'})
    
    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password
        )
                
        if not user:
            raise serializers.ValidationError('Usuario no autenticado', code='authorization')
        
        data['user'] = user
        return data
    
    
class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True, write_only=True)
    new_password = serializers.CharField(required=True, write_only=True)
    
    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError("La contraseña actual es incorrecta")
        return value
    
    def validate_new_password(self, value):
        return value
    

class PasswordResetRequestSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    
 
class PasswordResetConfirmSerializer:
    new_password = serializers.CharField(required=True)
       
    

    
    