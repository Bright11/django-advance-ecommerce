from django.shortcuts import render,redirect
from django.views import View
# Create your views here.
from .forms import CategoryForm,SubcatsForm,ProductForm
from . models import *
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import logout


class adminaddcat(View):
    def get(self,request):
        if not request.user.is_superuser:
            return redirect('/')
            
        categoryform=CategoryForm()
        context={'categoryform':categoryform,'title':'Add category'}
        return render(request,'pages/adminaddcat.html',context)
    
    def post(self, request):
        categoryform=CategoryForm(request.POST)
        if categoryform.is_valid():
            categoryform.save()
            return redirect('adminapp:adminaddcat')
        else:
              return redirect('adminapp:adminaddcat')
        


class updatecategory(View):
    def get(self,request,pk):
        if not request.user.is_superuser:
            return redirect(request.META.get('HTTP_REFERER','/'))
        get_cart_by_id=get_object_or_404(Category,pk=pk)
        form=CategoryForm(instance=get_cart_by_id)
        context={"form":form,"get_cart_by_id":get_cart_by_id}
        return render(request,'pages/update_category.html',context)
    def post(self,request,pk):
        if not request.user.is_superuser:
            return redirect(request.META.get('HTTP_REFERER','/'))
        
        get_cart_by_id=get_object_or_404(Category,pk=pk)
        form=CategoryForm(request.POST,instance=get_cart_by_id)
        if form.is_valid():
            form.save()
            return redirect("adminapp:adminaddcat")
        else:
            return redirect(request.META.get('HTTP_REFERER','/'))
        
class deletecategory(View):
    def get(self,request,pk):
        if not request.user.is_superuser:
            return redirect(request.META.get('HTTP_REFERER','/'))
        get_object_or_404(Category,pk=pk).delete()
        return redirect(request.META.get('HTTP_REFERER','/'))
    

class subcategory(View):
    def get(self,request):
        if not request.user.is_superuser:
            return redirect(request.META.get('HTTP_REFERER','/'))
        subform=SubcatsForm()
        getsubcategory=Subcategory.objects.all()
        context={"subcat":getsubcategory,'subform':subform}
        return render(request,'pages/viewsubcategory.html',context)
    
    def post(self, request):
        if not request.user.is_superuser:
            return redirect(request.META.get('HTTP_REFERER','/'))
        subform=SubcatsForm(request.POST)
        if subform.is_valid():
            subform.save()
            return redirect('adminapp:viewsubcategory')
        else:
            return redirect('adminapp:viewsubcategory')
        

class updatesubcategory(View):
    def get(self,request,pk):
        if not request.user.is_superuser:
            return redirect(request.META.get('HTTP_REFERER','/'))
        subcategory=get_object_or_404(Subcategory,pk=pk)
        form=SubcatsForm(instance=subcategory)
        context={"form":form,'subcategory':subcategory}
        return render(request,'pages/update_subcategory.html',context)
    
    def post(self,request,pk):
        if not request.user.is_superuser:
            return redirect(request.META.get('HTTP_REFERER','/'))
        subcategory=get_object_or_404(Subcategory,pk=pk)
        form=SubcatsForm(request.POST,instance=subcategory)
        if form.is_valid():
            form.save()
            return redirect('adminapp:viewsubcategory')
        else:
             return redirect(request.META.get('HTTP_REFERER','/'))
         
class deletesubcategory(View):
    def get(self,request,pk):
        if not request.user.is_superuser:
            return redirect(request.META.get('HTTP_REFERER','/'))
        get_object_or_404(Subcategory,pk=pk).delete()
        return redirect(request.META.get('HTTP_REFERER','/'))
    
    
        









    