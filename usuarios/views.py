from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.tokens import default_token_generator
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.urls import reverse

from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework import status

from .serializers import RegisterUserSerializer, AuthTokenSerializer, ChangePasswordSerializer, PasswordResetRequestSerializer, PasswordResetConfirmSerializer

class RegisterUserView(generics.CreateAPIView):
    serializer_class = RegisterUserSerializer
    permission_classes = [permissions.IsAuthenticated]
    

class RetrieveUserView(generics.UpdateAPIView):
    serializer_class = RegisterUserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    def get_object(self):
        return self.request.user
    

class CreateTokenView(ObtainAuthToken):
    serializer_class = AuthTokenSerializer


class DeleteUserView(generics.RetrieveUpdateAPIView):
    serializer_class = RegisterUserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    def put(self, request, user_id):
        try:
            user = get_user_model().objects.get(id=user_id)
            user.is_active = False
            user.save()
            return redirect(reverse('UserLogin'))
        except get_user_model().DoesNotExist:
            return Response({"error": "El usuario no existe."}, status=status.HTTP_404_NOT_FOUND)
        

class LoginView(generics.GenericAPIView):
    serializer_class = RegisterUserSerializer
    
    def post(self, request):
        
        email = request.data.get('email', None)
        password = request.data.get('password', None)
        user = authenticate(email=email, password=password)
    
        if user:            
            login(request, user)
            return Response({"message": "Inicio de sesion"}, status=status.HTTP_200_OK)
        
        return Response({"message": "credenciales invalidas"}, status=status.HTTP_401_UNAUTHORIZED)      


class LogoutView(generics.GenericAPIView):
    def post(self, request):
        logout(request)
        
        #return Response({"message": "Cierre de sesion"}, status=status.HTTP_200_OK)
        return redirect(reverse('UserLogin'))
    
class ChangePasswordView(generics.GenericAPIView):
    serializer_class = ChangePasswordSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
        
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        user = request.user
        user.set_password(serializer.validated_data['new_password'])
        user.save()
        
        return Response({"message": "Contraseña actualizada correctamente"}, status=status.HTTP_200_OK)  
    
    
User = get_user_model

class PasswordResetRequestView(generics.GenericAPIView):
    serializre_class= PasswordResetRequestSerializer
    
    def post(self, request, *arg, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validates_data('email')
        
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({ 'error':"El usuario con este correo no existe"}, status=status.HTTP_400_BAD_REQUEST)
        
        token = default_token_generator.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        reset_url = request.build_absolute_url(reverse('PasswordResetConfirm', kwargs={'uidb64': uid, 'token': token}))
        
        subject = "Restablecimiento de la contraseña"
        message = render_to_string('password_reset_email.html', {
            'user': user,
            'reset_url': reset_url,
        })
        
        send_mail(subject, message, 'from@example.com', [user.email])
        
        return Response({"message":"Se ha enviado un correo electronico para restablecer la contraseña"}, status=status.HTTP_200_OK)
    
        
class PasswordResetConfirm(generics.GenericAPIView):
    serializer_class = PasswordResetConfirmSerializer
    
    def post(self, request, uidb64, token, *args, **kwargs):
        
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
            
        if user is not None and default_token_generator.check_token(user, token):
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            new_password = serializer.validated_data['new_password']
            user.set_password(new_password)
            user.save()
            return Response ({"message": "contraseña restablecida correctamente"}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "El enlace no es valido"}, status=status.HTTP_400_BAD_REQUEST)
     
    
        

             
    
    



