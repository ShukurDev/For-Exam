

from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import *
from .serializers import *


# Create your views here.

@api_view(['GET'])
def ProductAPI(request):
    product = Product.objects.all()

    serializer = ProductSerializer(product, many=True)

    return Response(serializer.data)


@api_view(['GET','POST'])
def CreateProductAPI(request):

    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET','POST'])
def CreateDeliverAPI(request):

    serializer = DeliverSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        
    return Response(serializer.data)


@api_view(['GET','POST'])
def CreateCategoryAPI(request):
    
    serializer = CategorySerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET','POST'])
def CreateOrderAPI(request):
    serializer = OrderSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)



# @api_view(['GET'])
# def listcategory(request,pk):
#     product = Productitem.objects.get(id=pk)
#     name = product.name
#     all_count = Productitem.quantity
#     all_pay = Productitem.get_total
#
#
# @api_view(['GET'])
# def productitemlist(request,pk):
#     product = Product.objects.get(id=pk)
#     productitm = Order.objects.get(id=pk)
#     quantity = productitm.quantity
#     print(productitm.id)
    
#     if quantity>0:
#         serializer = Productitm(productitm,many=True)
#         return Response(serializer.data)
#     else:
#         serializer = ProductSerializer(product,many=True)
#         return Response(serializer.data)
# @api_view(['GET'])
# def Result(request):
#     product_count = Productitem.quantity
#     product_pay = Productitem.get_total
#     serializer = ProductResult(product_pay,product_count,many=True)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)


class ResultListView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
