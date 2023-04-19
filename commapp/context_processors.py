from django.views import View
from adminapp .models import Category,Subcategory,Wishlist
def category(request):
	category=Category.objects.all()
	categorytopbar=Category.objects.filter(categories__isnull=False).distinct()
	subcategory=Subcategory.objects.all()
	if request.user.is_authenticated:
		getwishlist=Wishlist.objects.filter(user=request.user).count()
	else:
		getwishlist=0

	return{'category':category,'subcategory':subcategory,'categorytopbar':categorytopbar,'getwishlist':getwishlist}