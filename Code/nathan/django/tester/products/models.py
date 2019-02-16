from django.db import models


#
# class Cart(models.Model):
#     title       = models.CharField(max_length=120)
#     description = models.TextField(blank=True, null=True)
#     price       = models.DecimalField(decimal_places=2, max_digits=10000)
#     featured    = models.BooleanField()

class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10000)
    featured = models.BooleanField()
    # in_cart = models.BooleanField()
    # cart = models.ForeignKey(Cart, on_delete=models.CASCADE)