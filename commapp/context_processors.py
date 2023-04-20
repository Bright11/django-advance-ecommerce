from django.views import View
from adminapp .models import Category,Subcategory,Wishlist,Cart
def category(request):
	category=Category.objects.all()
	categorytopbar=Category.objects.filter(categories__isnull=False).distinct()
	subcategory=Subcategory.objects.all()
	if request.user.is_authenticated:
		getwishlist=Wishlist.objects.filter(user=request.user).count()
		countcart=Cart.objects.filter(users=request.user).count()

	else:
		getwishlist=0
		countcart=0

	return{'category':category,'subcategory':subcategory,'categorytopbar':categorytopbar,'getwishlist':getwishlist,'countcart':countcart}