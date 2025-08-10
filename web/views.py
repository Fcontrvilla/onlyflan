from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Producto
from django.views.generic import DetailView

# Create your views here.

def home(request):
    flanes = Producto.objects.all().filter(premium = False)
    return render(request, "web/home.html", {"flanes":flanes})

@login_required
def home_premium(request):
    flanes = Producto.objects.all().filter(premium = True)
    return render(request, "web/home_premium.html", {"flanes":flanes})


#def detalle(request):
 #   flanes = Producto.objects.all()
  #  return render(request, "web/detalle_producto.html", {"flanes":flanes})


def detalle(request, producto_id):
    # Usa get_object_or_404 para buscar el flan por su ID.
    # Si no lo encuentra, automáticamente devuelve un error 404.
    flan = get_object_or_404(Producto, id=producto_id)
    
    # Renderiza la plantilla `detalle_flan.html` y le pasa el objeto 'flan'
    return render(request, 'web/detalle_producto.html', {"flan":flan})