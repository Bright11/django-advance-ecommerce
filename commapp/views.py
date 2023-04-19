from django.shortcuts import render,redirect
from django.views import View
from adminapp .models import Category,Product,Subcategory
# Create your views here.

class index(View):
    def get(self,request):
        products=Product.objects.all()
        subcat=Subcategory.objects.filter(category__isnull=False).distinct()
        context={'title':'home','products':products,'subcat':subcat}
        return render(request,'pages/index.html',context)


# getting products by categories

class getcategory(View):
    def get(self,request,category):
        getbycategory=Product.objects.filter(category=category)
        context={'product':getbycategory,'title':'Categories'}
        return render(request,'pages/viewcategory.html',context)