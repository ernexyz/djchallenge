from products.models import Product
from products.serializers import ProductSerializer
from rest_framework import generics
from rest_framework_bulk import ListCreateBulkUpdateAPIView


class ProductList(ListCreateBulkUpdateAPIView):
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
