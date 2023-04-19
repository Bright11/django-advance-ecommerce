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