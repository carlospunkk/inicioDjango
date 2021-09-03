"""novo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
#from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import url,include

'''exibir  ARQUIVOS html'''
#from django.views.generic import TemplateView

#criando rotas
urlpatterns = [
    #tela admin
    url('admin/', admin.site.urls),
    #tela app accounts
    url(r'accounts/', include("accounts.urls"))

     #criando rota para a pagina inicial 
    #url('',TemplateView.as_view(template_name='home.html')),
   
]
