from operator import mod
from django.db import models

class Product(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    price=models.FloatField()
    image=models.ImageField(upload_to="media/products")