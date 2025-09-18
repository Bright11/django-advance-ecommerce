from django.shortcuts import render,redirect
from django.views import View
# Create your views here.
from .forms import CategoryForm,SubcatsForm,RegisterForm,ProductForm
from . models import *
from django.shortcuts import render, get_object_or_404, redirect


from django.contrib.auth import logout
class adminaddcat(View):
    def get(self,request):
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
        
class viewcategory(View):
    def get(self,request):
        category=Category.objects.all()
        context={"category":category}
        return render(request,'pages/adminviewcategory.html',context)

class updatecategory(View):
    def get(self,request,pk):
        get_cart_by_id=get_object_or_404(Category,pk=pk)
        form=CategoryForm(instance=get_cart_by_id)
        context={"form":form,"get_cart_by_id":get_cart_by_id}
        return render(request,'pages/update_category.html',context)
    def post(self,request,pk):
        
        get_cart_by_id=get_object_or_404(Category,pk=pk)
        form=CategoryForm(request.POST,instance=get_cart_by_id)
        if form.is_valid():
            form.save()
            return redirect("adminapp:viewcategory")
        else:
            return redirect(request.META.get('HTTP_REFERER','/'))
        
class deletecategory(View):
    def get(self,request,pk):
        get_object_or_404(Category,pk=pk).delete()
        return redirect(request.META.get('HTTP_REFERER','/'))
    
# adding subcategory into database
class adminsubcats(View):
    def get(self,request):
        subform=SubcatsForm()
        context={'subform':subform}
        return render(request,'pages/adminsubcats.html',context)

    def post(self, request):
        subform=SubcatsForm(request.POST)
        if subform.is_valid():
            subform.save()
            return redirect('adminapp:adminsubcats')
        else:
            return redirect('adminapp:adminsubcats')
        
class viewsubcategory(View):
    def get(self,request):
        getsubcategory=Subcategory.objects.all()
        context={"subcat":getsubcategory}
        return render(request,'pages/viewsubcategory.html',context)
    
class updatesubcategory(View):
    def get(self,request,pk):
        subcategory=get_object_or_404(Subcategory,pk=pk)
        form=SubcatsForm(instance=subcategory)
        context={"form":form,'subcategory':subcategory}
        return render(request,'pages/update_subcategory.html',context)
    
    def post(self,request,pk):
        subcategory=get_object_or_404(Subcategory,pk=pk)
        form=SubcatsForm(request.POST,instance=subcategory)
        if form.is_valid():
            form.save()
            return redirect('adminapp:viewsubcategory')
        else:
             return redirect(request.META.get('HTTP_REFERER','/'))
         
class deletesubcategory(View):
    def get(self,request,pk):
        get_object_or_404(Subcategory,pk=pk).delete()
        return redirect(request.META.get('HTTP_REFERER','/'))
    
    
        
# registration forms
class registeruser(View):
    def get(self,request):
        registerform=RegisterForm()
        context={'registerform':registerform,'title':'registration'}
        return render(request,'pages/registeruser.html',context)
    def post(self,request):
        registerform=RegisterForm(request.POST)
        if registerform.is_valid():
            registerform.save()
            return redirect('adminapp:login')
        else:
            return redirect('adminapp:registeruser')
        

# logout

def logoutuser(request):
    logout(request)
    return redirect('adminapp:login')








    