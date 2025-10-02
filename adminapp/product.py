from django.shortcuts import render,redirect
from django.views import View
# Create your views here.
from .forms import CategoryForm,SubcatsForm,ProductForm
from . models import *
from django.shortcuts import render, get_object_or_404, redirect

# adding product
class addproduct(View):
    def get(self,request):
        proform=ProductForm()
        context={'title':'Add product','proform':proform}
        return render(request,'pages/addproduct.html',context)

    def post(self,request):
        proforms=ProductForm(request.POST,request.FILES)
        if proforms.is_valid():
            proforms.save()
            return redirect('adminapp:addproduct')
        else:
            print('not saved')
            return redirect('adminapp:addproduct')

class getallproduct(View):
    def get(self,request):
        if not request.user.is_superuser:
            return redirect('commapp:index')
        products=Product.objects.all()
        context={"products":products}
        return render(request,"pages/viewproducts.html",context)
    
class updateproduct(View):
    def get(self,request,pk):
        singlepro=get_object_or_404(Product,pk=pk)
        # get categories which is from subcategories
        form=ProductForm(instance=singlepro)
        context={"form":form,'singlepro':singlepro}
        return render(request,"pages/update_product.html",context)
    
    def post(self,request,pk):
        singlepro=get_object_or_404(Product,pk=pk)
        form = ProductForm(request.POST, request.FILES, instance=singlepro)
        if form.is_valid():
            form.save()
            return redirect("adminapp:viewproduct")
        else:
            return redirect(request.META.get('HTTP_REFERER','/'))
    
class deleteview(View):
    def get(self,request,pk):
       deletepro=get_object_or_404(Product,pk=pk)
    #    for deleting image
       if deletepro.image and os.path.isfile(deletepro.image.path):
           os.remove(deletepro.image.path)
       deletepro.delete()
        # print(pk)
       return redirect(request.META.get('HTTP_REFERER','/'))
        