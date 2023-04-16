from django import forms
from .models import Category

class CategoryForm(forms.ModelForm):
	class Meta:
		model=Category
		fields=('name',)
		name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Category name'}))
		