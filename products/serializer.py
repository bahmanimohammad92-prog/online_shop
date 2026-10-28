from .models import Category, Product, ProductImage
from rest_framework import serializers

class CategorySerializers(serializers.ModelSerializer):

    class Meta:
        
        model = Category
        fields = "__all__"


class ProductSerializers(serializers.ModelSerializer):
     
     class Meta:
        
         model = Product
         fields = "__all__"


class ProductImageSerializers(serializers.ModelSerializer):

    class Meta:

        model = ProductImage
        fields = "__all__"

        # بعدا فیلدها رو بهش بده ک چک کنهاز all استفاده نکن
