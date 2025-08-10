
from django.urls import path
from .views import home, home_premium, detalle


urlpatterns = [
    path("", home, name ="home"),
    path("premium/", home_premium, name ="home_premium"),
    path('detalle/<int:producto_id>/', detalle, name='detalle')
    
   
]
