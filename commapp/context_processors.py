from django.views import View
from adminapp .models import Category,Subcategory
def category(request):
	category=Category.objects.all()
	subcategory=Subcategory.objects.all()
	return{'category':category,'subcategory':subcategory}