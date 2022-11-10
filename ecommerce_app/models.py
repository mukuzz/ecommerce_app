from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User

class UserProfile(models.Model):
    mobile_number = models.CharField(max_length=10, primary_key=True)
    profile_image = models.ImageField()
    address = models.CharField(max_length=256)
    user_auth = models.OneToOneField(User, on_delete=models.CASCADE)
    

class Product(models.Model):
    name = models.CharField(max_length=256)
    type = models.CharField(max_length=256)
    category = models.CharField(max_length=256)
    description = models.TextField()
    quantity = models.IntegerField()
    price = models.FloatField()
    seller = models.ForeignKey(UserProfile, on_delete=models.CASCADE)


class ListedProducts(models.Model):
    listed_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField()


class CartItem(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()


class Transaction(models.Model):
    order_id = models.UUIDField()
    seller = models.ForeignKey(UserProfile, on_delete=models.PROTECT, related_name="seller")
    buyer = models.ForeignKey(UserProfile, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    price = models.FloatField()
    order_time = models.DateTimeField(default=timezone.now)
    shipment_time = models.DateTimeField(default=timezone.now)