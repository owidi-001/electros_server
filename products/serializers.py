from dataclasses import field
from rest_framework import serializers
from .models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=['id','name','logo']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        # fields=['id','label','category','description','price','image']
        fields = '__all__'
        depth = 1