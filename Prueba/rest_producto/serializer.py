from dataclasses import fields
from rest_framework import serializers
from core.models import Producto
class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields =['sku','nombreProducto','descripcion',
                'urlimg','precio','stock','categoria']