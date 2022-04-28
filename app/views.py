from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'app/index.html')

def gatos1 (request):
    return render(request, 'app/gatos1.html')

def perro1 (request):
    return render(request, 'app/perro1.html')


def exotico1 (request):
    return render(request, 'app/exotico1.html')




def sinregistro (request):
    return render(request, 'app/sinregistro.html')

def perro1con (request):
    return render(request, 'app/perro1con.html')

def gatos1con (request):
    return render(request, 'app/gatos1con.html')

def exotico1con (request):
    return render(request, 'app/exotico1con.html')
    
def fundacion (request):
    return render(request, 'app/fundacion.html')

def historial (request):
    return render(request, 'app/historial.html')

def segui (request):
    return render(request, 'app/segui.html')

def vercarro (request):
    return render(request, 'app/vercarro.html')

