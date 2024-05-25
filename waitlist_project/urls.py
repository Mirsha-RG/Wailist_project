
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from formulario.views import CreateFormularioView, RetriveFormularioView 
from listas.views import CreateListaView, RetriveListaView, ListListaView, ExportarListaCSVAPIView, ToggleListaView
from usuarios.views import (RegisterUserView, RetrieveUserView, CreateTokenView, DeleteUserView, LoginView, LogoutView, 
                            ChangePasswordView, PasswordResetRequestView, PasswordResetConfirm, )
from perfil.views import CreatePerfilAPIView, RetrivePerfilAPIView
from metricas.middlewares import MetricsMiddlewareFormulario, MetricsMiddlewareLista
from pagina.views import CreateLandingPageAPIView, RetriveLandingPageAPIView, ToggleLandingPageView



urlpatterns = [ 
    
    path('admin/', admin.site.urls),
    
    path('post/', CreateFormularioView.as_view(), name='CreateFormulario'),
    path('get/', RetriveFormularioView.as_view(), name='RetriveFormulario'),
    path('put/<int:formulario_id>', RetriveFormularioView.as_view(), name='UpdateFormulario'),
    path('delete/<int:formulario_id>', RetriveFormularioView.as_view()),
    
    path('post/lista', CreateListaView.as_view(), name='CreateLista'),
    path('get/lista', RetriveListaView.as_view(), name='RetriveListado'),
    path('list_lista/', ListListaView.as_view(), name='Listado total'),
    path('csv_lista/', ExportarListaCSVAPIView.as_view(), name='DescargarLista'),
    path('get_lista/<int:lista_id>', RetriveListaView.as_view(), name='RetriveListaId'),
    path('put_lista/<int:lista_id>', RetriveListaView.as_view(), name='UpdateLista'),
    path('delete_lista/<int:lista_id>', RetriveListaView.as_view(), name='DeleteLista'),
    path('privacidad_lista/<int:lista_id>', ToggleListaView.as_view(), name='PrivacidadLista'),
    
    
    path('post_user/', RegisterUserView.as_view(), name='RegistroUsuario'),
    path('put/<int:pk>/', RetrieveUserView.as_view(), name='UpdateUser'),
    path('token/', CreateTokenView.as_view(), name='CreateToken'),
    path('delete/<int:user_id>/', DeleteUserView.as_view(), name='DeleteUser'),  
    path('login/', LoginView.as_view(), name='UserLogin'),  
    path('logout/', LogoutView.as_view(), name='UserLogout'),
    path('change_password/', ChangePasswordView.as_view(), name='ChangePassword'),
    path('password_reset/', PasswordResetRequestView.as_view(), name='PasswordReset'),
    path('password_rest_confirm/<uidb64>/<token>/', PasswordResetConfirm.as_view(), name='UserLogout'),
    
    path('post_perfil/', CreatePerfilAPIView.as_view(), name='CreatePerfil'),
    path('get_perfil/', RetrivePerfilAPIView.as_view(), name='RetrivePerfil'),
    path('put_perfil/<int:perfil_id>', RetrivePerfilAPIView.as_view(), name='UpdatePerfil'),
    path('delete_perfil/<int:perfil_id>', RetrivePerfilAPIView.as_view(), name='DeletePerfil'),
    
    
    path('metricas_formulario/', MetricsMiddlewareFormulario.as_view(), name='Metricasformulario'),
    path('metricas_lista/', MetricsMiddlewareLista.as_view(), name='MetricasLista'),
    
    path('create_landing_page/', CreateLandingPageAPIView.as_view, name='CreateLandingPage'),
    path('put_landing_page/', RetriveLandingPageAPIView.as_view, name='UpdateLandingPage'),
    path('privacidad_landing_page/<int:landing_page_id>/', ToggleLandingPageView.as_view, name='PrivacidadLandingPage'),
   
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

