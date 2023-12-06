from django.shortcuts import render
from django.db.models import Q

def home(request):
    title = "Home"
    return render(request, 'almacen/inicio.html')

def mantenedor(request):
    title = "Mantenedor de materiales"
    return render(request, 'almacen/mm.html')

def despacho_m(request):
    title = "Despacho de materiales"
    return render(request, 'almacen/dm.html')

def listado_p(request):
    title = "Listado de productos"
    return render(request, 'almacen/lp.html')

def despacho_a(request):
    title = "Despachos anteriores"
    return render(request, 'almacen/da.html')

def listado_d(request):
    title = "Listado de despachos"
    return render(request, 'almacen/ld.html')
