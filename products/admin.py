from django.contrib import admin

from .models import Product, ProductDetail


admin.site.register(Product)
admin.site.register(ProductDetail)
