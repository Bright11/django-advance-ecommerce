from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from adminapp .models import Category,Product,Subcategory,Wishlist,Cart
# Create your views here.

class index(View):
    def get(self,request):
        products=Product.objects.all()
        subcat=Subcategory.objects.filter(category__isnull=False).distinct()
        context={'title':'home','products':products,'subcat':subcat}
        return render(request,'pages/index.html',context)


# getting products by categories

class getcategory(View):
    def get(self,request,category):
        getbycategory=Product.objects.filter(category=category)
        context={'product':getbycategory,'title':'Categories'}
        return render(request,'pages/viewcategory.html',context)
    


# product details
class details(View):
    def get(self,request,pdetails):
        details=get_object_or_404(Product,pk=pdetails)
        details.views +=1
        details.save()
        context={'details':details}
        return render(request,'pages/details.html',context)
    

# product wishlist
class wishlist(View):
    def get(self,request,pk):
        if request.user.is_authenticated:
            # if authenticated
            # check if item is on the wishlist
            checkproduct=Product.objects.get(pk=pk)
            checkwishlist=Wishlist.objects.filter(product_id=checkproduct,user=request.user).exists()
            if checkwishlist:
                # if we have item in wishlist
                print('yes item exists')
                return redirect('commapp:index')
            else:
                # if no item in wishlist
                print('added to wishlist')
                newwishlist=Wishlist.objects.create(product_id=checkproduct,user=request.user)
                newwishlist.save()
                return redirect('commapp:index')
        
            # if not authenticated
        else:
            return redirect('addminapp:login')
        

# wishlist data
class mywishlist(View):
    def get(self,request):
        if request.user.is_authenticated:
            getuserwishlist=Wishlist.objects.filter(user=request.user)
            context={'getuserwishlist':getuserwishlist,'title':'My Wishlist'}
            return render(request,'pages/mywishlist.html',context)
        else:
            return redirect('addminapp:login')
        


# items cart
class mycart(View):
    def get(self,request):
        if request.user.is_authenticated:
            mycart=Cart.objects.filter(user=request.user)
            context={'mycart':mycart}
            return render(request,'pages/mycart.html',context)
        else:
            return redirect('addminapp:login')