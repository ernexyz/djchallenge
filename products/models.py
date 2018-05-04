from django.db import models


class Product(models.Model):
    TYPE_CHOICES = (
        ('PR', 'PR'),
        ('SR', 'SR'),
    )
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    type = models.CharField(max_length=2,
                            choices=TYPE_CHOICES,
                            default='PR')
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    is_variation = models.BooleanField(default=False)
    brand_id = models.IntegerField()
    code = models.IntegerField(unique=True)
    family = models.IntegerField()
    is_complement = models.BooleanField(default=False)
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class ProductDetail(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_visibility = models.BooleanField(default=True)
    price = models.FloatField()
    price_offer = models.FloatField(null=True)
    offer_day_from = models.DateTimeField(null=True)
    offer_day_to = models.DateTimeField(null=True)
    quantity = models.IntegerField()
    sku = models.IntegerField(unique=True)
    product = models.OneToOneField(Product,
                                   related_name='detail',
                                   on_delete=models.CASCADE)
