from django.shortcuts import get_list_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .models import Perfil
from .serializers import PerfilSerializer

class CreatePerfilAPIView(APIView):
    permission_classes = (IsAuthenticated, )  
    
    def post(self, request):
        data = request.data
        serializer = PerfilSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({ 'message':'creado'}, status=status.HTTP_200_OK)
    

class RetrivePerfilAPIView(APIView):
    permission_classes = (IsAuthenticated, )
    
    def get(self, request, perfil_id):
        perfil_object = get_list_or_404(Perfil, pk=perfil_id)
        serializer = PerfilSerializer(perfil_id)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put (self, request, perfil_id):
        perfil_object = get_list_or_404(Perfil,pk= perfil_id)
        serializer = PerfilSerializer(instance=perfil_object, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, perfil_id):
        perfil_object = get_list_or_404(Perfil,pk= perfil_id)
        perfil_object.status=False
        perfil_object.save()
        return Response({'message': 'Eliminado correctamente'}, status=status.HTTP_204_NO_CONTENT)
    
    

    
    
    
    
    
    

# Create your views here.
