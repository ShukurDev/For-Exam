from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import *


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

# class ProductResult(serializers.ModelSerializer):
#     class Meta:
#         product_count = serializers.IntegerField()
#         product_pay = serializers.DecimalField(max_digits=20, decimal_places=0)

class ProductitemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields =('quantity','get_total') # kerakli fieldlar

    def get_total(self, obj):
        
        return obj.get_total


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class DeliverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deliver
        fields = '__all__'
class Productitm(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        