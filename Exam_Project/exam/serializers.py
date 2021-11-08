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

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('product','product_name', 'jami_soni','jami_summa')  # kerakli fieldlar

    def product_name(self, obj):
        return obj.product_name

    def jami_summa(self, obj):
        return obj.jami_summa

class ManyIncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['product','product_name','foyda']

    def product_name(self, obj):
        return obj.product_name

    def foyda(self,obj):

        return obj.foyda


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

# class OrderItem(serializers.ModelSerializer):
#     class Meta:
#         model =

class DeliverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deliver
        fields = '__all__'


# class ProductAllSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = ['name', 'total_product','total_summa']
#
#
#     def total_product(self, obj):
#         return obj.total_product
#
#     def total_summa(self, obj):
#         return obj.total_summa
