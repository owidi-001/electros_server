from django.urls import path
from .views import product_list,product_detail

urlpatterns=[
    path('products/',product_list,'products'),
    path('products/<int:id>/',product_detail,'product_details'),
]