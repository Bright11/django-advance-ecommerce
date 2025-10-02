from django.shortcuts import render
from authapp.forms import *
from django.views import View
from django.shortcuts import render,redirect
from django.contrib.auth import logout
# Create your views here.


# registration forms
# class registeruser(View):
#     def get(self,request):
#         registerform=RegisterForm()
#         context={'registerform':registerform,'title':'registration'}
#         return render(request,'pages/registeruser.html',context)
#     def post(self,request):
#         registerform=RegisterForm(request.POST)
#         if registerform.is_valid():
#             registerform.save()
#             return redirect('authapp:login')
#         else:
#             return redirect('authapp:registeruser')


# another way of writing registration forms
class registeruser(View):
    def get(self,request):
        registerform=RegisterForm()
        context={'registerform':registerform,'title':'registration'}
        return render(request,'pages/registeruser.html',context)
    def post(self,request):
        registerform=RegisterForm(request.POST)
        if registerform.is_valid():
            print('form is valid')
            user = registerform.save(commit=False)
            user.email = registerform.cleaned_data.get('email').lower()
            user.is_superuser = True
            user.is_staff = True
            user.save()
            # registerform.save()
            return redirect('authapp:login')
        else:
            print('form is not valid',registerform.errors)
            return redirect('authapp:registeruser')
    
# logout

def logoutuser(request):
    logout(request)
    return redirect('authapp:login')

class deleteview(View):
    def get(self,request):
        if not request.user.is_authenticated:
            return redirect("authapp:login")
        user = request.user
        user.delete()
        return redirect("authapp:index")