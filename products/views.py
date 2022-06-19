from ssl import HAS_ECDH
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Product
from .serializers import ProductSerializer

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
    


