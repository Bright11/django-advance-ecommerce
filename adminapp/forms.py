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



	# produvt model form
class ProductForm(forms.ModelForm):
	class Meta:
		model=Product
		fields=('name','price','category','keywords','description','views','image')
		
		exclude=['views']
		





