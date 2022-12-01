from django.shortcuts import render
from mobi.decorators import detect_mobile

# Create your views here.

@detect_mobile
def PagPrincipal(request):
    if request.mobile:
        
        contexto2 = {
        "IsMovile" : True
        }

    else:
        contexto2 = {
        "IsMovile" : False
        }

        #Hacer cosas para otros dispositivos
    
    return render(request, 'PagPrincipal.html',contexto2)
