from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path(r'api/addCategory/', views.addCategory),
    path('api/category/<id>/', views.category),
    path('api/addProduct/', views.addProduct),
    path('api/product/<id>/', views.product),
    path('api/productList/', views.product_list),
    path('api/categoryList/', views.category_list),
]