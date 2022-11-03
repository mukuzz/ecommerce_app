from django.db import models

class User(models.Model):
    pass

class Seller(User):
    pass

class Customer(User):
    pass

class Item(models.Model):
    pass