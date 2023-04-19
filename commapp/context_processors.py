from django.views import View
from adminapp .models import Category,Subcategory
def category(request):
	category=Category.objects.all()
	categorytopbar=Category.objects.filter(categories__isnull=False).distinct()
	subcategory=Subcategory.objects.all()
	return{'category':category,'subcategory':subcategory,'categorytopbar':categorytopbar}