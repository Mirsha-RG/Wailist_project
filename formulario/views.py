
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .models import Formulario
from .serializers import FormularioSerializer

# Create your views here.

class CreateFormularioView(APIView):
    permission_classes = (AllowAny,)  
          
    def post(self, request):
        data = request.data
        serializer = FormularioSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()      
        return Response({'message': 'Creado'}, status=status.HTTP_201_CREATED) 

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