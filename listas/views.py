from django.shortcuts import render

from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import Lista
from .serializers import ListaSerializer


class CreateListaView(APIView):
    permission_classes = (IsAuthenticated,)  
    
    def post(self, request):
        
        
        data = request.data
        serializer = ListaSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()      
        return Response({'message': 'Creado'}, status=status.HTTP_201_CREATED) 
    
    
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
    
      



