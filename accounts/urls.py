#criando rotas para accounts

from django.conf.urls import url

#chamando o arquivo views que esta dentro dos arquivos dentro do accounts 
from . import views



#criando rotas
urlpatterns = [
   
url(r'$^', views.PaginaInicial),
url(r'^login/',views.PaginaLogin),
url(r'^registro/',views.Registro),
   
]