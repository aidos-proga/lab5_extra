from django.http import JsonResponse
from django.shortcuts import render
from .models import Product, Category


# Create your views here.


def getProductList(request):
    datas = Product.objects.all()

    data_list = [
        {
            'id': p.id,
            'name': p.name,
            'price': p.price,
            'description': p.description,
            'count': p.count,
            'is_active': p.is_active,
        } for p in datas
    ]

    return JsonResponse(data_list, safe=False)


def getProduct(request, *args, **kwargs):
    data = Product.objects.get(id=int(kwargs['id']))

    data_list = {
        'id': data.id,
        'name': data.name,
        'price': data.price,
        'description': data.description,
        'count': data.count,
        'is_active': data.is_active,
    }

    return JsonResponse(data_list, safe=False)


def getCategoryList(request):
    datas = Category.objects.all()

    data_list = [
        {
            'id': i.id,
            'name': i.name,
        } for i in datas
    ]
    return JsonResponse(data_list, safe=False)


def getCategory(request, *args, **kwargs):
    datas = Category.objects.get(id=int(kwargs['id']))

    data_list = {
        'id': datas.id,
        'name': datas.name,
    }

    return JsonResponse(data_list, safe=False)


def getByCategory(request, *args, **kwargs):
    datas = Product.objects.filter(category__id=int(kwargs['id']))

    data_list = [
        {
            'category_id': i.category.id,
            'category_name': i.category.name,
            'product_id': i.id,
            'product_name': i.name,
            'product_price': i.price,
            'product_description': i.description,
            'product_count': i.count,
            'product_is_active': i.is_active
        }for i in datas
    ]

    return JsonResponse(data_list, safe=False)



