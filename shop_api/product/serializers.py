from rest_framework import serializers
from .models import Product, Category, Review

class ProductReviewSerializer(serializers.ModelSerializer):
        rating = serializers.SerializerMethodField()  #для средней оценки

        class Meta:
                model = Product
                fields = ['title', 'reviews', 'rating']
                depth = 1

        def get_rating (self, obj):
                return obj.rating()

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
        product_count = serializers.SerializerMethodField()

        class Meta:
                model = Category
                fields = '__all__'

        def get_product_count(self, category):
                return category.product_count()



class ProductDetailSerializer(serializers.ModelSerializer):
        class Meta:
                model = Product
                fields = '__all__'




class ProductListSerializer(serializers.ModelSerializer):
        reviews = serializers.SerializerMethodField()  #чтобы вывести наименования а не просто id

        class Meta:
                model = Product
                fields = ['id', 'title', 'price', 'description', 'reviews']
                # fields = 'id title price description'.split
                # fields = '__all__'
                # exclude = ['id', 'price']
                # depth = 1
        
        def get_reviews (self, product):
                return product.review_list()
        