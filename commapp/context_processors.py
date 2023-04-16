from django.views import View
from adminapp .models import Category
def category(request):
	category=Category.objects.all()
	return{'category':category}