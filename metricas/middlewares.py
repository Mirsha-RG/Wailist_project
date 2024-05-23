import requests
from django.contrib.gis.geoip2 import GeoIP2
from django.utils.deprecation import MiddlewareMixin

from .models import VisitasFormulario, VisitasLista



class MetricsMiddlewareFormulario(MiddlewareMixin):
    
    def process_request(self, request):
        user_agent = request.META.get('HTTP_USER_AGENT','')
        browser = self.get_browser(user_agent)
        os = self.get_os(user_agent)
        device = self.get_device(user_agent)
        ip = self.get_client_ip(request)
        country, city = self.get_location(ip)
        
        VisitasFormulario.objects.create(
            ip=ip,
            browser=browser,
            os=os,
            device=device,
            country=country,
            city=city,
            path=request.path,        
            
        )
        
    def get_browser(self, user_agent):   
        if 'Chrome' in user_agent:
            return 'Chrome'
        elif 'Firefox' in user_agent:
            return 'Firefox'
        elif 'Safari' in user_agent:
            return 'Safari'
        elif 'Edge' in user_agent:
            return 'Edge'
        else:
            return 'Other'
        
    def get_os(self, user_agent):   
        if 'Windows' in user_agent:
            return 'Windows'
        elif 'Linux' in user_agent:
            return 'Linux'
        elif 'macOs' in user_agent:
            return 'macOs'
        elif 'Android' in user_agent:
            return 'Android'
        elif 'iOS' in user_agent:
            return 'iOS'
        else:
            return 'Other'
        
    def get_device(self, user_agent):   
        if 'Mobile' in user_agent:
            return 'Mobile'
        else:
            return 'Desktop'
    
    def get_client_ip(self, request):   
        
      x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')#request.META es un diccionario que contiene todas las cabeceras HTTP y metadatos de la solicitud.
      
      if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0] #divide la cadena x_forwarded_for en una lista de direcciones IP, utilizando la coma como delimitador.
      else:
            ip = request.META.get('REMOTE_ADDR')
      return ip
      
      
    def get_location(self, ip):
        g = GeoIP2()
        
        try:
            location = g.city(ip)
            return location('country_name'), location('city')
        except Exception:
            return None, None
        
        

class MetricsMiddlewareLista(MiddlewareMixin):
    
    def process_request(self, request):
        user_agent = request.META.get('HTTP_USER_AGENT','')
        browser = self.get_browser(user_agent)
        os = self.get_os(user_agent)
        device = self.get_device(user_agent)
        ip = self.get_client_ip(request)
        country, city = self.get_location(ip)
        
        VisitasLista.objects.create(
            ip=ip,
            browser=browser,
            os=os,
            device=device,
            country=country,
            city=city,
            path=request.path,        
            
        )
        
    def get_browser(self, user_agent):   
        if 'Chrome' in user_agent:
            return 'Chrome'
        elif 'Firefox' in user_agent:
            return 'Firefox'
        elif 'Safari' in user_agent:
            return 'Safari'
        elif 'Edge' in user_agent:
            return 'Edge'
        else:
            return 'Other'
        
    def get_os(self, user_agent):   
        if 'Windows' in user_agent:
            return 'Windows'
        elif 'Linux' in user_agent:
            return 'Linux'
        elif 'macOs' in user_agent:
            return 'macOs'
        elif 'Android' in user_agent:
            return 'Android'
        elif 'iOS' in user_agent:
            return 'iOS'
        else:
            return 'Other'
        
    def get_device(self, user_agent):   
        if 'Mobile' in user_agent:
            return 'Mobile'
        else:
            return 'Desktop'
    
    def get_client_ip(self, request):   
        
      x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')#request.META es un diccionario que contiene todas las cabeceras HTTP y metadatos de la solicitud.
      
      if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0] #divide la cadena x_forwarded_for en una lista de direcciones IP, utilizando la coma como delimitador.
      else:
            ip = request.META.get('REMOTE_ADDR')
      return ip
      
      
    def get_location(self, ip):
        g = GeoIP2()
        
        try:
            location = g.city(ip)
            return location('country_name'), location('city')
        except Exception:
            return None, None