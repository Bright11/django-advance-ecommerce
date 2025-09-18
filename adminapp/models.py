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
