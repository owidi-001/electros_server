from django.urls import path
from .views import category_list, category_products, product_list,product_detail

urlpatterns=[
    # product routes
    path('products/',product_list,name='products'),
    path('products/<int:id>/',product_detail,name='product_details'),

    # Categorical data routes
    path('categories/',category_list,name='categories'),
    path('categories/<str:name>/',category_products,name='category_products'),

]