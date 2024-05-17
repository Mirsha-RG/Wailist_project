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
from listas.views import CreateListaView, RetriveListaView
from usuarios.views import RegisterUserView, RetrieveUserView, CreateTokenView, DeleteUserView, LoginView, LogoutView


urlpatterns = [ 
    
    path('admin/', admin.site.urls),
    
    path('post/', CreateFormularioView.as_view(), name='CreateFormulario'),
    path('get/', RetriveFormularioView.as_view(), name='RetriveFormulario'),
    path('put/<int:formulario_id>', RetriveFormularioView.as_view(), name='UpdateFormulario'),
    path('delete/<int:formulario_id>', RetriveFormularioView.as_view()),
    
    path('post/lista', CreateListaView.as_view(), name='CreateLista'),
    path('get/lista', RetriveListaView.as_view(), name='RetriveListado'),
    path('get_lista/<int:lista_id>', RetriveListaView.as_view(), name='RetriveListaId'),
    path('put_lista/<int:lista_id>', RetriveListaView.as_view(), name='UpdateLista'),
    path('delete_lista/<int:lista_id>', RetriveListaView.as_view(), name='DeleteLista'),
    
    path('post_user/', RegisterUserView.as_view(), name='RegistroUsuario'),
    path('put/<int:pk>/', RetrieveUserView.as_view(), name='UpdateUser'),
    path('token/', CreateTokenView.as_view(), name='CreateToken'),
    path('delete/<int:user_id>/', DeleteUserView.as_view(), name='DeleteUser'),  
    path('login/', LoginView.as_view(), name='UserLogin'),  
    path('logout/', LogoutView.as_view(), name='UserLogout'),
       
   
]

