from django.contrib import admin
from .models import Category, Subcategory
# Register your models here.
admin.site.register([Category,Subcategory])