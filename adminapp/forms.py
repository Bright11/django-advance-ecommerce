from django import forms
from .models import Category,Subcategory,Product,Cart,Wishlist
# 
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
# catgeory form
class CategoryForm(forms.ModelForm):
	class Meta:
		model=Category
		fields=('name',)
		name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Category name'}))


# subcategory form
class SubcatsForm(forms.ModelForm):
	class Meta:
		model=Subcategory
		fields=('subname','category_id')
		subname=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Subcategory name'}))
		category_id=forms.CharField(widget=forms.Select())


# registeration
class RegisterForm(UserCreationForm):
	class Meta:
		model=User
		fields=('username','email','password1','password2')
		username=forms.TextInput(attrs={'placeholder':'User Name'})
		email=forms.CharField(max_length=200,required=True, widget=forms.EmailInput(attrs={"placeholder": "Enter your email!"}))
		password1=forms.PasswordInput(attrs={'placeholder':'paasword***'})
		password2=forms.PasswordInput(attrs={'placeholder':'confirm paasword***'})

class LoginForm(AuthenticationForm):
	username=forms.CharField(max_length=200,required=True, widget=forms.TextInput(attrs={'placeholder':'username'}))
	password=forms.CharField(max_length=200,required=True,widget=forms.PasswordInput(attrs={'placeholder':'Password'}))



	# produvt model form
class ProductForm(forms.ModelForm):
	class Meta:
		model=Product
		fields=('name','price','category','keywords','description','views','image')
		# name=forms.CharField(required=True,max_length=100,widget=(forms.TextInput(attrs={'placeholder':'product name'})))
		# price=forms.CharField(required=True,max_length=100, widget=(forms.TextInput(attrs={'placeholder':'product price'})))
		# category=forms.CharField(required=True,max_length=100, widget=(forms.Select(attrs={'placeholder':'product Category'})))
		# keywords=forms.CharField(required=True,max_length=100, widget=(forms.Textarea(attrs={'placeholder':'product details'})))
		# description=forms.CharField(required=True,max_length=100, widget=(forms.Textarea(attrs={'placeholder':'product keywords'})))
		# image=forms.CharField(required=True,widget=forms.ImageField)
		exclude=['views']
		





