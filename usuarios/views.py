from django.contrib.auth import get_user_model, authenticate, login, logout
from django.shortcuts import redirect
from django.urls import reverse

from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework import status

from .serializers import RegisterUserSerializer, AuthTokenSerializer

class RegisterUserView(generics.CreateAPIView):
    serializer_class = RegisterUserSerializer
    

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
        
        
    
        

             
    
    



