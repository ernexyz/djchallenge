from rest_framework import serializers
from products.models import Product, ProductDetail


class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDetail
        fields = (
            'id', 'is_active', 'is_visibility', 'price', 'price_offer', 'offer_day_from', 'offer_day_to',
            'quantity', 'sku',
        )


class ProductSerializer(serializers.ModelSerializer):
    detail = DetailSerializer(required=False)

    class Meta:
        model = Product
        fields = (
            'id', 'is_active', 'type', 'name', 'description', 'is_variation', 'brand_id', 'code', 'family',
            'is_complement', 'is_delete', 'detail',
        )

    def create(self, validated_data):
        detail_data = validated_data.pop('detail')
        product = Product.objects.create(**validated_data)
        ProductDetail.objects.create(product=product, **detail_data)
        return product

    def update(self, instance, validated_data):
        if 'detail' in validated_data:
            detail_data = validated_data.pop('detail')
            try:
                detail = instance.detail
                detail.is_active = detail_data.get('is_active', detail.is_active)
                detail.is_visibility = detail_data.get('is_visibility', detail.is_visibility)
                detail.price = detail_data.get('price', detail.price)
                detail.price_offer = detail_data.get('price_offer', detail.price_offer)
                detail.offer_day_from = detail_data.get('offer_day_from', detail.offer_day_from)
                detail.offer_day_to = detail_data.get('offer_day_to', detail.offer_day_to)
                detail.quantity = detail_data.get('quantity', detail.quantity)
                detail.sku = detail_data.get('sku', detail.sku)
                detail.save()
            except ProductDetail.DoesNotExist:
                detail_serializer = DetailSerializer(data=detail_data)
                detail_serializer.is_valid(raise_exception=True)
                ProductDetail.objects.create(product=instance, **detail_data)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.type = validated_data.get('type', instance.type)
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.is_variation = validated_data.get('is_variation', instance.is_variation)
        instance.brand_id = validated_data.get('brand_id', instance.brand_id)
        instance.code = validated_data.get('code', instance.code)
        instance.family = validated_data.get('family', instance.family)
        instance.is_complement = validated_data.get('is_complement', instance.is_complement)
        instance.is_delete = validated_data.get('is_delete', instance.is_delete)
        instance.save()
        return instance
