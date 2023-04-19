from django.db import models
from django.contrib.auth.models import User
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
      price=models.CharField(max_length=200)
      category=models.ForeignKey(Subcategory,related_name='category',on_delete=models.CASCADE)
      keywords=models.TextField()
      description=models.TextField()
      image=models.ImageField(upload_to='image')
      views=models.IntegerField(default=0)
      def __str__(self):
            return self.name 

class Cart(models.Model):
      product_id=models.ForeignKey(Product,related_name='product',on_delete=models.CASCADE)
      tottalprice=models.CharField(max_length=255)
      qty=models.IntegerField(default=1)
      user=models.ForeignKey(User,on_delete=models.CASCADE)
      def __str__(self):
            return self.product_id.name


class Wishlist(models.Model):
      product_id=models.ForeignKey(Product,related_name='products',on_delete=models.CASCADE)
      user=models.ForeignKey(User,on_delete=models.CASCADE)
      def __str__(self):
            return self.product_id.name
