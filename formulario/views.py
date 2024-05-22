from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

from usuarios.models import User
from listas.models import Lista
from .models import Formulario
from .serializers import FormularioSerializer

# Create your views here.

class CreateFormularioView(APIView):
    permission_classes = (IsAuthenticated,)      
    
    def post(self, request):
        user = request.user
        
        total_registros = Formulario.objects.filter(user=User).count()
    
        if total_registros >= 500:
                    return Response({'message': 'Has superado el limite de mensajes contratados'}, status=status.HTTP_400_BAD_REQUEST)           
    
        data = request.data
        serializer = FormularioSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()      
        return Response({'message': 'Creado'}, status=status.HTTP_201_CREATED) 
    
    def send_confirmation_email(self, formulario, listas):     
        
        
        subject = 'Confirmacion de registro'      
        message = f'Hola {formulario.usuario} \n\n,{listas.message} \n\nAqui estan los detalles de tu registro: \n\n{formulario.usuario} \nEmail: {formulario.email} \nTeléfono: {formulario.phone} \n\nSaludos.\nEl equipo de {listas.usuario} ' 
        from_email = settings.EMAIL_HOST_USER   
        to_email = [formulario.email]
        
        send_mail(subject, message, from_email, to_email, fail_silently=False)
        

class RetriveFormularioView(APIView):
    permission_classes = (AllowAny, )
    
    def get (self,request):
        formulario_list = Formulario.objects.all()
        serializer = FormularioSerializer(formulario_list, many=True)
        return Response(serializer.data)
        
        
    def put(self, request, formulario_id ):
        formulario_obj = get_object_or_404(Formulario, pk=formulario_id)
        serializer = FormularioSerializer(instance=formulario_obj, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save() 
        return Response(serializer.data, status=status.HTTP_200_OK)
        
     
    def delete(self, request, formulario_id):
        formulario_obj = get_object_or_404(Formulario, pk=formulario_id)
        formulario_obj.status=False
        formulario_obj.save()
        return Response ({'mesage':'Eliminado'}, status=status.HTTP_204_NO_CONTENT)
    
    
"""
    
    def get(self, request, formulario_id):
        formulario_obj = get_object_or_404(Formulario, id=formulario_id)
        serializer = FormularioSerializer(formulario_obj)
        
        return Response (serializer.data, status=status.HTTP_200_OK) 
        """