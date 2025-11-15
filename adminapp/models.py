from django.db import models
from django.contrib.auth.models import User
import os 
from django.conf import settings

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=200,unique=True)
    def __str__(self):
        return self.name 
    
class Subcategory(models.Model):
        category_id=models.ForeignKey(Category,related_name='categories',on_delete=models.CASCADE)
        subname=models.CharField(max_length=200,unique=True)
        def __str__(self):
                return self.subname
        

# product models
class Product(models.Model):
      name=models.CharField(max_length=255)
      price=models.PositiveIntegerField()
      bought_price=models.PositiveIntegerField(null=True,blank=True)
      category=models.ForeignKey(Subcategory,related_name='category',on_delete=models.CASCADE)
      keywords=models.TextField()
      description=models.TextField()
      image=models.ImageField(upload_to='image')
      views=models.IntegerField(default=0)
      
      # delete image when image is changed
      def save(self, *args, **kwargs):
        try:
            old_item = Product.objects.get(pk=self.pk)
            if old_item.image and old_item.image != self.image:
                old_image_path = old_item.image.path
                if os.path.exists(old_image_path):
                    os.remove(old_image_path)
        except Product.DoesNotExist:
            pass  # this is a new object, so no old image
        super().save(*args, **kwargs)
      
      def __str__(self):
            return self.name 

class Cart(models.Model):
      product_id=models.ForeignKey(Product,related_name='product',on_delete=models.CASCADE)
      tottalprice=models.PositiveIntegerField()
      qty=models.IntegerField(default=1)
      users=models.ForeignKey(User,related_name='users', on_delete=models.CASCADE)
      def __str__(self):
            return self.product_id.name


class Wishlist(models.Model):
      product_id=models.ForeignKey(Product,related_name='products',on_delete=models.CASCADE)
      user=models.ForeignKey(User,related_name='user', on_delete=models.CASCADE)
      def __str__(self):
            return self.product_id.name



class Address(models.Model):
      address_id=models.CharField(max_length=200)
      user=models.ForeignKey(User,related_name='users_address', on_delete=models.CASCADE)
      address=models.TextField()
      landmark=models.TextField(max_length=200,blank=True,null=True)
      phone=models.CharField(max_length=15)
      ordered_date=models.DateTimeField(auto_now_add=True)
      status=models.BooleanField(default=False)
      
      def __str__(self):
            return self.address_id



class OrderedItems(models.Model):
      address=models.ForeignKey(Address,related_name='user_address',on_delete=models.CASCADE)
      product_id=models.ForeignKey(Product,related_name='user_products',on_delete=models.CASCADE)
      price=models.PositiveIntegerField()
      qty=models.IntegerField()
      user=models.ForeignKey(User,related_name='users_order', on_delete=models.CASCADE)
      def __str__(self):
            return f"{self.product_id.name} ({self.qty})"
      
      def total_price(self):
            return self.qty * self.price

class PaymentRecord(models.Model):
      # address=models.ForeignKey(Address,related_name='user_address',on_delete=models.CASCADE)
      user=models.ForeignKey(User, related_name='users_payment', on_delete=models.CASCADE)
      total_amount=models.CharField(max_length=100)
      transaction_id=models.CharField(max_length=200)
      paid=models.BooleanField(default=False)
      currency=models.CharField(max_length=100)
      description=models.CharField(max_length=200, blank=True,null=True)
      email=models.CharField(max_length=200)
      
      def __str__(self):
            return self.user.username