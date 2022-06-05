from rest_framework import serializers
from . models import ProductItem


class ProductItemSerializer(serializers.ModelSerializer):
    
    model = ProductItem
    fields='__all__'







