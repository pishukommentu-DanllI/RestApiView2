from rest_framework import serializers
from .models import *


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Product


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Order
