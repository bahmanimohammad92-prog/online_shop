from .models import Category, Product, ProductImage
from rest_framework import serializers

class CategorySerializers(serializers.ModelSerializer):

    class Meta:
        
        model = Category
        fields = [
            "title", "slug"
            ]


class ProductSerializers(serializers.ModelSerializer):
     
     class Meta:
        
         model = Product
         fields = [
            "category", "name", "price", "stock", "discount_price", 
            "slug", "description", "is_active", "created_at"
            ]


class ProductImageSerializers(serializers.ModelSerializer):

    class Meta:

        model = ProductImage
        fields = [
            "image", "product", "is_primary", "sort_order"
            ]
