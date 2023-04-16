from django.shortcuts import render,redirect
from django.views import View
# Create your views here.
from .forms import CategoryForm

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