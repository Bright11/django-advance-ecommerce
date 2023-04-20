from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from adminapp .models import Category,Product,Subcategory,Wishlist,Cart
# Create your views here.
from django.db.models import Max
class index(View):
    def get(self,request):
        products=Product.objects.all()
        highlyviewed = Product.objects.annotate(max_views=Max('views')).order_by('-max_views')[0:4]
        subcat=Subcategory.objects.filter(category__isnull=False).distinct()
        context={'title':'home','products':products,'subcat':subcat,'items':highlyviewed}
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
            checkcart=Cart.objects.filter(product_id=checkproduct,users=request.user).exists()
            if checkcart:
                return redirect('commapp:index')
            else:
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
            return redirect('adminapp:login')
        

# wishlist data
class mywishlist(View):
    def get(self,request):
        if request.user.is_authenticated:
            getuserwishlist=Wishlist.objects.filter(user=request.user)
            context={'getuserwishlist':getuserwishlist,'title':'My Wishlist'}
            return render(request,'pages/mywishlist.html',context)
        else:
            return redirect('addminapp:login')
        
# add to cart
class addtocart(View):
    def get(self,request,cartid):
        if request.user.is_authenticated:
           
            checkitem=Product.objects.get(pk=cartid)

            checkcart=Cart.objects.filter(product_id=checkitem,users=request.user).exists()
            checkwishlist=Wishlist.objects.filter(product_id=checkitem,user=request.user).exists()
            if checkcart:
                # item is in the cart
                updatecart=get_object_or_404(Cart,product_id=checkitem,users=request.user)
                updatecart.tottalprice +=checkitem.price
                updatecart.qty +=1
                
                updatecart.save()
                return redirect('commapp:index')
            else:
                #no item in cart
                addcart=Cart.objects.create(product_id=checkitem,tottalprice=checkitem.price,qty=1,users=request.user)
                addcart.save()
                if checkwishlist:
                    get_object_or_404(Wishlist,product_id=checkitem,user=request.user).delete()
                    return redirect('commapp:index')
                else:
                    return redirect('commapp:index')

        else:
            return redirect('adminapp:login')



# getting items cart
class mycart(View):
    def get(self,request):
        if request.user.is_authenticated:
            mycart=Cart.objects.filter(users=request.user)
            context={'mycart':mycart}
            return render(request,'pages/mycart.html',context)
        else:
            return redirect('addminapp:login')
        

# DELETE CART

class deletecart(View):
    def get(self,request,pk):
        print('delete pass')
        deletecarts=get_object_or_404(Cart,users=request.user,pk=pk).delete()
        if deletecarts:
            return redirect('commapp:mycart')
        else:
            return redirect('commapp:mycart')


# remove from wishlist

class deletewishlist(View):
    def get(self,request,pk):
        print('delete pass')
        deletecarts=get_object_or_404(Wishlist,user=request.user,pk=pk).delete()
        if deletecarts:
            return redirect('commapp:mycart')
        else:
            return redirect('commapp:mycart')