from datetime import timedelta
from django.utils import timezone
from django.shortcuts import redirect

class CheckSubscriptionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call__(self, request):
       if request.user.is_authenticated:
            if not request.user.is_paid:
                free_period_end = request.user.date_joined + timedelta(days=30)
                if timezone.now() > free_period_end:
                    return redirect('payment_page')  # Redirigir a la página de pago  
                
       response = self.get_response(request)
       return response