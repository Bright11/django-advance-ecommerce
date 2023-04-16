from django.db import models

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