"""
URL configuration for waitlist_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from formulario.views import CreateFormularioView, RetriveFormularioView 
from listas.views import CreateListaView, RetriveListaView, ListListaView, ExportarListaCSVAPIView
from usuarios.views import (RegisterUserView, RetrieveUserView, CreateTokenView, DeleteUserView, LoginView, LogoutView, 
                            ChangePasswordView, PasswordResetRequestView, PasswordResetConfirm, )
from perfil.views import CreatePerfilAPIView, RetrivePerfilAPIView


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
    
       
   
]

