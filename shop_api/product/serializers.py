from rest_framework import serializers
from .models import Product, Category, Review

class ReviewDetailSerializer(serializers.ModelSerializer):
        class Meta:
                model = Review
                fields = '__all__'


class ReviewListSerializer(serializers.ModelSerializer):
        class Meta:
                model = Review
                fields = '__all__'


class CetegoryDetailSerializer(serializers.ModelSerializer):
        class Meta:
                model = Category
                fields = '__all__'


class CategoryListSerializer(serializers.ModelSerializer):
        class Meta:
                model = Category
                fields = '__all__'



class ProductDetailSerializer(serializers.ModelSerializer):
        class Meta:
                model = Product
                fields = '__all__'




class ProductListSerializer(serializers.ModelSerializer):
        class Meta:
                model = Product
                fields = ['id', 'title', 'price', 'description']
                # fields = 'id title price description'.split
                # fields = '__all__'
                # exclude = ['id', 'price']