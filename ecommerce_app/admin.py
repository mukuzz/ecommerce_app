from django.contrib import admin
from .models import UserProfile, CartItem, Product, ListedProducts, Transaction

admin.site.register(UserProfile)
admin.site.register(CartItem)
admin.site.register(Product)
admin.site.register(ListedProducts)
admin.site.register(Transaction)