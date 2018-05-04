from products.models import Product
from products.serializers import ProductSerializer, DetailSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import status


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    name = 'product-list'
    filter_fields = ('type', 'name', 'brand_id', 'code', 'family')
    search_fields = ('^name', 'description')
    ordering_fields = ('name',)


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    name = 'product-detail'
