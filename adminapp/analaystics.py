from .models import *
from django.contrib.auth.models import User
from django.db.models import Sum

def analaytics(request):
    number_of_p= Product.objects.count()
    users=User.objects.count()
    product_selling_total= Product.objects.aggregate(price=Sum('price'))['price'] or 0
    product_bought_total= Product.objects.aggregate(bought_price=Sum('bought_price'))['bought_price'] or 0
    total_order= PaymentRecord.objects.aggregate(total_amount=Sum('total_amount'))['total_amount'] or 0
    profit=product_bought_total - product_selling_total 
    
    
    return{'number_of_p':number_of_p,'users':users,"product_selling_total":product_selling_total,"profit":profit,'product_bought_total':product_bought_total}