
from django.urls import path

from .views import  PagPrincipal

urlpatterns = [

    path('',PagPrincipal,name="PagPrincipal"),





]