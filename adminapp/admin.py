from django.contrib import admin
from .models import Category, Subcategory, Product, Cart, Wishlist
# Register your models here.
admin.site.register([Category,Subcategory,Product, Cart, Wishlist])