from django.shortcuts import render, HttpResponse

# Create your views here.
def PaginaInicial(request) :
    return render(request,"apaccounts/home.html")
def PaginaLogin(request):
    return render(request,"apaccounts/login.html")
def Registro(request) :
    return render(request,"apaccounts/registro.html")