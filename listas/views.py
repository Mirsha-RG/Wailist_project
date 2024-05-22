from django.shortcuts import render
from django.http import HttpResponse
import csv

from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import Lista
from .serializers import ListaSerializer, ListListaSerializer


class CreateListaView(APIView):
    permission_classes = (IsAuthenticated, )  
    
    def post(self, request):        
        
        data = request.data
        serializer = ListaSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()      
        return Response({'message': 'Creado'}, status=status.HTTP_201_CREATED) 
    
    
class ListListaView(APIView):
       permission_classes = (IsAuthenticated, )  
       
       def get(self,request):
           lista_list = Lista.objects.all()
           serializer = ListListaSerializer(lista_list, many=True)
           return Response (serializer.data, status=status.HTTP_200_OK)      
    
    
class RetriveListaView(APIView):
    permission_classes = (AllowAny, )
    
    def get(self,request):
        lista_list = Lista.objects.all()
        serializer = ListaSerializer(lista_list, many=True)
        return Response(serializer.data)  
    
    def get(self, request, lista_id):
        lista_obj = get_object_or_404(Lista, id=lista_id)
        serializer = ListaSerializer(lista_obj)        
        return Response (serializer.data, status=status.HTTP_200_OK) 
    
    def put(self, request, lista_id ):
        lista_obj = get_object_or_404(Lista, pk=lista_id)
        serializer = ListaSerializer(instance=lista_obj, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save() 
        return Response(serializer.data, status=status.HTTP_200_OK) 
    
    def delete(self, request, lista_id):
        lista_obj = get_object_or_404(Lista, pk=lista_id)
        lista_obj.status=False
        lista_obj.save()
        return Response ({'mesage':'Eliminado'}, status=status.HTTP_204_NO_CONTENT)     
    
    
class ExportarListaCSVAPIView(APIView):
    permission_classes = (IsAuthenticated, )
    
    def get (self, request):        
        # Obtener las listas del usuario autenticado
        listas = Lista.objects.filter(usuario=request.user)
        # Crear una respuesta HTTP con el tipo de contenido CSV
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="listas.csv"'
        # Crear un escritor CSV
        writer = csv.writer(response)
        # Escribir la fila de encabezado
        writer.writerow(['ID', 'Nombre', 'Descripción', 'Activa/Pausa', 'Fecha de Creación', 'Estatus'])
        # Escribir las filas de datos
        for lista in listas:
            writer.writerow([
                lista.id, 
                lista.name, 
                lista.description, 
                lista.is_active, 
                lista.created_date, 
                lista.status
            ])
        
        return response
        
        
         
    
    
      



