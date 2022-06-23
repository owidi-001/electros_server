from email import message
from itertools import product
from ssl import HAS_ECDH
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer

@csrf_exempt
def category_list(request):
    """
    List of all categories
    """
    if request.method=='GET':
        categories=Category.objects.all()
        serializer=CategorySerializer(categories,many=True)
        return JsonResponse(serializer.data)

@csrf_exempt
def category_products(request,category_name):
    """
    List all products of the given category
    """
    if request.method=='GET':
        category=Category.objects.filter(name=category_name)[0]
        
        if category:
            products=Product.objects.filter(category=category)
            serializer=ProductSerializer(products,many=True)
            return JsonResponse(serializer.data)
        return HttpResponse(message="Products not found",status=404)


@csrf_exempt
def product_list(request):
    """
    List all products or create one
    """
    if request.method=='GET':
        products=Product.objects.all()
        serializer=ProductSerializer(products,many=True)
        return JsonResponse(serializer.data,safe=False)

    elif request.method=='POST':
        data=JSONParser().parse(request)
        serializer=ProductSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors,status=400)


@csrf_exempt
def product_detail(request,pk):
    """
    Retrieve, Update, Delete a product given the product key
    """
    try:
        product=Product.objects.get(id=pk)
    except Product.DoesNotExist:
        return HttpResponse(message="Product not found",status=404)
    
    if request.method=="GET":
        serializer=ProductSerializer(product)
        return JsonResponse(serializer.data,status=200)
    elif request.method=="PUT":
        data=JSONParser.parse(request)
        serializer=ProductSerializer(product,data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors,status=400)
    elif request.method=='DELETE':
        product.delete()
        return HttpResponse(status=204)
    


