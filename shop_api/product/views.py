from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product, Category, Review
from .serializers import (
    ProductListSerializer, ProductDetailSerializer,
    CategoryListSerializer, CetegoryDetailSerializer,
    ReviewListSerializer, ReviewDetailSerializer,
    ProductReviewSerializer
    )

@api_view(['GET'])
def product_review_api_view(request):
    products = Product.objects.all()


    list_ = ProductReviewSerializer(instance=products, many=True).data

    return Response(
        data=(list_),    
        status=status.HTTP_200_OK,
    ) 


@api_view(['GET'])
def review_detail_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': 'Review not found'})
    item = ReviewDetailSerializer(review, many=False).data
    return Response(data=item, status=status.HTTP_200_OK)



@api_view(['GET'])
def review_list_api_view(request):
    reviews = Review.objects.all()
    list_ = ReviewListSerializer(reviews, many=True).data
    return Response(data=list_, status=status.HTTP_200_OK)


@api_view(['GET'])
def category_detail_api_view(request, id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': 'Product not found'})
    item = CetegoryDetailSerializer(category, many=False).data
    return Response(data=item, status=status.HTTP_200_OK)



@api_view(['GET'])
def category_list_api_view(request):
    categories = Category.objects.all()
    list_ = CategoryListSerializer(instance=categories,many=True).data
    return Response(
        data=list_,
        status=status.HTTP_200_OK
    )


@api_view(['GET'])
def product_detail_api_view(request,id):
    try:
        product = Product.objects.get(id=id)     #DoesNotExist / MultiKeyError
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error':'Product not found'})
    item = ProductDetailSerializer(product, many=False).data
    return Response(data=item, status=status.HTTP_200_OK)


@api_view(http_method_names=["GET"])
def product_list_api_view(request):
    # step 1. Collect films from DF (QuerySet)
    products = Product.objects.all()

    # step 2. Reformat QuerySet to list of dictionaries (Serializer)
    list_ = ProductListSerializer(instance=products, many=True).data

    # step 3. Return Response
    return Response(
        data=list_,      #dict, list (int str bool dict)
        status=status.HTTP_200_OK,          #int 100 200 300 400 500
    )

