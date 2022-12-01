from django.shortcuts import render
from mobi.decorators import detect_mobile

# Create your views here.

@detect_mobile
def PagPrincipal(request):
    if request.mobile:
        IsMovile = True
    else:
        IsMovile = False
        #Hacer cosas para otros dispositivos
    print(IsMovile)
    return render(request, 'PagPrincipal.html')
