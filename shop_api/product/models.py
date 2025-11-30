from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title
    

class Review(models.Model):
    text = models.TextField(null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.text