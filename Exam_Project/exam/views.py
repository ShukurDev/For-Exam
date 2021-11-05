

from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import *
from .serializers import *


# Create your views here.
def console(request):
    category = Category.objects.all()
    # categoryid = category.name
    # print(categoryid)
    context = {
        'category':category
    }
    return render(request,'index.html',context)

@api_view(['GET'])
def Productapi(request):
    product = Product.objects.all()
    serializer = ProductSerializer(product, many=True)

    return Response(serializer.data)


class ResultListView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = ProductitemSerializer

@api_view(['GET'])
def Result(request):
    product_count = Productitem.quantity
    product_pay = Productitem.get_total
    serializer = ProductResult(product_pay,product_count,many=True)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET','POST'])
def createproduct(request):

    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def createdeliver(request):
    if request.method == "POST":
        serializer = DeliverSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)


@api_view(['POST'])
def createproductitem(request):
        serializer = ProductitemSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)


@api_view(['POST'])
def createcategory(request):
    if request.method == "POST":
        serializer = CategorySerializer(data=request.data)
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
@api_view(['GET'])
def productitemlist(request,pk):
    product = Product.objects.get(id=pk)
    productitm = Order.objects.get(id=pk)
    quantity = productitm.quantity
    print(productitm.id)
    
    if quantity>0:
        serializer = Productitm(productitm,many=True)
        return Response(serializer.data)
    else:
        serializer = ProductSerializer(product,many=True)
        return Response(serializer.data)
