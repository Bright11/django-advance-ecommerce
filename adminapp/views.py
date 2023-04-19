from django.shortcuts import render,redirect
from django.views import View
# Create your views here.
from .forms import CategoryForm,SubcatsForm,RegisterForm,ProductForm

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
        

# registration forms
class registeruser(View):
    def get(self,request):
        registerform=RegisterForm()
        context={'registerform':registerform,'title':'registration'}
        return render(request,'pages/register.html',context)
    def post(self,request):
        registerform=RegisterForm(request.POST)
        if registerform.is_valid():
            registerform.save()
            return redirect('adminapp:login')
        else:
            return redirect('adminapp:register')
        

# logout

def logoutuser(request):
    logout(request)
    return redirect('adminapp:login')



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




# upload product

# def uploadproduct(request):
#     if request.method =="POST":
#         producform=ProductForm(request.POST, request.FILES)
#         if producform.is_valid():
#             producform.save()
#             return redirect('adminapp:addproduct')
#         else:
#             return redirect('adminapp:addproduct')

    