from django.shortcuts import render,redirect
from django.views import View
from adminapp .models import Category
# Create your views here.

class index(View):
    def get(self,request):
       
        context={'title':'home'}
        return render(request,'pages/index.html',context)