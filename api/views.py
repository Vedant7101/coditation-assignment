from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from api.models import Category, Product
from api.serializers import CategorySerializer, ProductSerializer
from rest_framework.decorators import api_view


def home(request):
    return render(request, 'home.html')


@api_view(['POST'])
def addCategory(request):
    if request.method == 'POST':
        category_data = JSONParser().parse(request)
        category_serializer = CategorySerializer(data=category_data)
        if category_serializer.is_valid():
            category_serializer.save()
            return JsonResponse({'message': 'Category added successfully!'}, status=status.HTTP_204_NO_CONTENT)
    return JsonResponse(category_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
def category(request, id):

    try:
        category = Category.objects.get(id=id)
    except ObjectDoesNotExist:
        return JsonResponse({'message': 'The category does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        category_serializer = CategorySerializer(product)
        return JsonResponse(category_serializer.data, safe=True)

    elif request.method == 'DELETE':
        category.delete()
        return JsonResponse({'message': 'Category was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def addProduct(request):
    if request.method == 'POST':
        product_data = JSONParser().parse(request)
        product_serializer = ProductSerializer(data=product_data)
        if product_serializer.is_valid():
            product_serializer.save()
            return JsonResponse({'message': 'Product added successfully!'}, status=status.HTTP_204_NO_CONTENT)
        return JsonResponse(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def product(request, id):
    try:
        product = Product.objects.get(id=id)
    except ObjectDoesNotExist:
        return JsonResponse({'message': 'The product does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        product_serializer = ProductSerializer(product)
        return JsonResponse(product_serializer.data, safe=True)

    elif request.method == 'PUT':
        product_data = JSONParser().parse(request)
        product_serializer = ProductSerializer(product, data=product_data)

        if product_serializer.is_valid():
            product_serializer.save()
            return JsonResponse({'message': 'Product updated successfully!'}, status=status.HTTP_204_NO_CONTENT)
        return JsonResponse(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        product.delete()
        return JsonResponse({'message': 'Product was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def product_list(request):
    if request.method == 'GET':
        if 'category' in request.GET:
            category = request.GET['category']
            product_data = Product.objects.filter(categories__contains=category)
        elif 'product_name' in request.GET:
            product = request.GET['product_name']
            product_data = Product.objects.filter(product_name=product)
        else:
            product_data = Product.objects.all()
        product_serializer = ProductSerializer(product_data, many=True)
        return JsonResponse(product_serializer.data, safe=False)


@api_view(['GET'])
def category_list(request):
    if 'category' in request.GET:
        categories = Category.objects.filter(category_name=request.GET['category'])
    else:
        categories = Category.objects.all()
    category_list = []
    for category in categories:
        sub_categories = list(Category.objects.filter(parent_category=category.category_name).values_list('category_name', flat=True))
        category_list.append({'id': category.id, 'category_name': category.category_name, 'sub_categories': sub_categories})
    return JsonResponse(category_list, safe=False)