from django.shortcuts import render

# Create your views here.


def PagPrincipal(request):
  
    return render(request, 'PagPrincipal.html')
