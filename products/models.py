from operator import mod
from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=200)
    logo=models.ImageField(upload_to="categories")

    def __str__(self):
        return self.name
        
    
class Product(models.Model):
    label = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    price=models.FloatField()
    image=models.ImageField(upload_to="products")
    quantity = models.IntegerField()    

    def __str__(self):
        return self.label