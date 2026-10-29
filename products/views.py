from django.shortcuts import get_object_or_404
from .serializer import ProductSerializers, ProductImageSerializers
from rest_framework.views import APIView 
from rest_framework.response import Response
from .models import Product
from rest_framework import status

class ProductAPIView(APIView):
    
    def get(self, request, slug):

        product = get_object_or_404(Product, slug=slug)
        serializers = ProductSerializers(product)
        return Response(serializers.data, status=status.HTTP_200_OK)




