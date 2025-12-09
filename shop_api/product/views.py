from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product, Category, Review
from .serializers import (
    ProductListSerializer, ProductDetailSerializer,
    CategoryListSerializer, CetegoryDetailSerializer,
    ReviewListSerializer, ReviewDetailSerializer,
    ProductReviewSerializer, ProductValidateSerializer,
    CategoryValidateSerializer, ReviewValidateSerializer,
    )

@api_view(['GET'])
def product_review_api_view(request):
    products = Product.objects.all()


    list_ = ProductReviewSerializer(instance=products, many=True).data

    return Response(
        data=(list_),    
        status=status.HTTP_200_OK,
    ) 


@api_view(['GET','PUT', 'DELETE'])
def review_detail_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': 'Review not found'})
    if request.method == 'GET':
        item = ReviewDetailSerializer(review, many=False).data
        return Response(data=item, status=status.HTTP_200_OK)
    elif request.method == 'PUT':

        serializer = ReviewValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        review.text = serializer.validated_data.get('text')
        review.stars = serializer.validated_data.get('stars')
        review.product_id = serializer.validated_data.get('product_id')
        review.save()
        return Response(status=status.HTTP_201_CREATED,
                        data=ReviewDetailSerializer(review).data)
    elif request.method == 'DELETE':
        review.delete()
        return Response (status=status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'POST'])
def review_list_api_view(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        list_ = ReviewListSerializer(reviews, many=True).data
        return Response(data=list_, status=status.HTTP_200_OK)
    elif request.method == 'POST':

        serializer = ReviewValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        text = serializer.validated_data.get('text')
        stars = serializer.validated_data.get('stars')
        product_id = serializer.validated_data.get('product_id')
        # product = Product.objects.get(id=product_id)
        review = Review.objects.create(
            text = text,
            stars = stars,
            product_id = product_id,
        )
        return Response(status=status.HTTP_201_CREATED,
                        data=ReviewDetailSerializer(review).data)




@api_view(['GET', 'PUT', 'DELETE'])
def category_detail_api_view(request, id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': 'Category not found'})
    if request.method == 'GET':
        item = CetegoryDetailSerializer(category).data
        return Response(data=item, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = CategoryValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        category.name = serializer.validated_data.get('name')
        category.save()
        return Response(status=status.HTTP_201_CREATED,
                        data=CetegoryDetailSerializer(category).data)
    elif request.method == 'DELETE':
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




@api_view(['GET', 'POST'])
def category_list_api_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        list_ = CategoryListSerializer(instance=categories,many=True).data
        return Response(
            data=list_,
            status=status.HTTP_200_OK
        )
    if request.method == 'POST':

        serializer = CategoryValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        name = serializer.validated_data.get('name')
        category = Category.objects.create(
            name=name,
        )
        return Response(status=status.HTTP_201_CREATED,
                        data=CetegoryDetailSerializer(category).data)





@api_view(['GET', 'PUT', 'DELETE'])
def product_detail_api_view(request,id):
    try:
        product = Product.objects.get(id=id)     #DoesNotExist / MultiKeyError
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error':'Product not found'})
    if request.method == 'GET':
        item = ProductDetailSerializer(product, many=False).data
        return Response(data=item, status=status.HTTP_200_OK)
    elif request.method == 'PUT':

        serializer = ProductValidateSerializer(data=request.data)   #укороченная версия
        serializer.is_valid(raise_exception=True)

        product.title = serializer.validated_data.get('title')
        product.description = serializer.validated_data.get('description')
        product.price = serializer.validated_data.get('price')
        product.category_id = serializer.validated_data.get('category_id')
        product.save()
        return Response(status=status.HTTP_201_CREATED,
                        data=ProductDetailSerializer(product).data)
    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




@api_view(http_method_names=["GET", 'POST'])
def product_list_api_view(request):
    if request.method == 'GET':
        # step 1. Collect films from DF (QuerySet)
        products = Product.objects.all()
        # step 2. Reformat QuerySet to list of dictionaries (Serializer)
        list_ = ProductListSerializer(instance=products, many=True).data
        # step 3. Return Response
        return Response(
            data=list_,      #dict, list (int str bool dict)
            status=status.HTTP_200_OK,          #int 100 200 300 400 500
        )
    elif request.method == 'POST':

        #Validation (existing typing extra)
        print('Некорректные:', request.data)
        serializer = ProductValidateSerializer(data=request.data)
        if not serializer.is_valid():  #длинная версия
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data=serializer.errors)
        print('Исправленные:', serializer.validated_data)

        title = serializer.validated_data.get('title')
        description = serializer.validated_data.get('description')
        price = serializer.validated_data.get('price')
        category_id = serializer.validated_data.get('category_id')

        products = Product.objects.create(
            title = title,
            description = description,
            price = price,
            category_id = category_id,
        )
        return Response (status=status.HTTP_201_CREATED,
                         data=ProductDetailSerializer(products).data)
