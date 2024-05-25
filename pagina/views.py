from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from perfil.models import Perfil
from perfil.serializers import PerfilSerializer

from .models import LandingPage
from .serializers import LandingPageSerializer

# Create your views here.

class CreateLandingPageAPIView(APIView):
    permission_classes = (IsAuthenticated, )  
    
    def post(self, request):
        data = request.data
        serializer = PerfilSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({ 'message':'creado'}, status=status.HTTP_200_OK)
    
 
class RetriveLandingPageAPIView(APIView):
    permission_classes = (IsAuthenticated, )
    
    def get(self, request, landing_page_id):
        landing_page_object = get_object_or_404(Perfil, pk=landing_page_id)
        serializer = LandingPageSerializer(landing_page_id)
        return Response(serializer.data, status=status.HTTP_200_OK)   

    def put (self, request, landing_page_id):
        landing_page_object = get_object_or_404(Perfil,pk= landing_page_id)
        serializer = LandingPageSerializer(instance=landing_page_object, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)    
    
    def delete(self, request, landing_page_id):
        landing_page_object = get_object_or_404(Perfil,pk= landing_page_id)
        landing_page_object.status=False
        landing_page_object.save()
        return Response({'message': 'Eliminado correctamente'}, status=status.HTTP_204_NO_CONTENT)    
    
    
class ToggleLandingPageView(APIView):
    permission_classes = (IsAuthenticated, )
    
    def post(self, request, lista_id, format=None):
        landng_page = LandingPage.objects.get(pk=lista_id)
        landng_page.is_active = not landng_page.is_active
        landng_page.save()
        return Response ({'message':'El estado de privacidad de la pagina se ha actualizado correctamente'}, status=status.HTTP_200_OK)
    
    
    