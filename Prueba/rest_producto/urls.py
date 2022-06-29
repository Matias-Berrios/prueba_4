from django.urls import path
from rest_producto.views import lista_productos, modificar_producto
from rest_producto.viewslogin import login

urlpatterns = [
    path('lista_productos', lista_productos, name='lista_productos'),
    path('modificar_producto/<id>', modificar_producto, name='modificar_producto'),
    path('login', login, name="login"),
]
