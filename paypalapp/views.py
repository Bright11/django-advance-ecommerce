# views.py
from django.shortcuts import redirect,render
from django.conf import settings
from django.http import HttpResponse
from django.urls import reverse
import paypalrestsdk
from adminapp.models import Cart,Address,PaymentRecord
from django.db.models import Sum
import uuid


# Configure PayPal SDK (you can also put this in settings.py)
paypalrestsdk.configure({
    "mode": "sandbox",  # or "live" for production
    "client_id": settings.PAYPAL_CLIENT_ID,
    "client_secret": settings.PAYPAL_CLIENT_SECRET,
})


def create_payment(request):
    
    # context = {
    #         "success": True,
    #         "user_email": 'user_email',
    #         "full_name": 'full_name',
    #         "transaction_id": 'transaction_id',
    #         "amount": 'total_amount',
    #         "currency":' currency',
    #         "description": 'description',
    #     }
    # return render(request, "pages/payment_success.html", context)
    # ✅ Dynamically generate return and cancel URLs
    if not request.user.is_authenticated:
        return redirect("authapp:login")
    user=request.user
    getchartdata=Cart.objects.filter(users=user)
    if not getchartdata:
        return redirect("commapp:index")
    try:
        Address.objects.filter(user=user).first()
    except Address.DoesNotExist:
        return redirect(request.META.get('HTTP_REFERER', '/'))
    return_url = request.build_absolute_uri(reverse('execute_payment'))
    cancel_url = request.build_absolute_uri(reverse('cancel_payment'))
    qty=Cart.objects.filter(users=user).count()
    total=getchartdata.aggregate(tottalprice=Sum('tottalprice'))['tottalprice'] or 0
    sku=str(uuid.uuid4().hex[:5]).upper()
    print("total",total,"qty",qty,"sku",sku)

    payment = paypalrestsdk.Payment({
        "intent": "sale",
        "payer": {
            "payment_method": "paypal"
        },
        "redirect_urls": {
            "return_url": return_url,
            "cancel_url": cancel_url,
        },
        "transactions": [{
            # "item_list": {
            #     "items": [{
            #         "name": "Test Product",
            #         "sku": sku,
            #         "price": total,
            #         "currency": "USD",
            #         "quantity": qty
            #     }]
            # },
            "amount": {
                "total": total,
                "currency": "USD"
            },
            "description": "Payment for test product"
        }]
    })

    if payment.create():
        # Redirect user to PayPal approval link
        for link in payment.links:
            if link.rel == "approval_url":
                return redirect(link.href)
        return HttpResponse("No approval URL found.")
    else:
        return HttpResponse(f"Payment creation failed: {payment.error}")


def execute_payment(request):
    payment_id = request.GET.get('paymentId')
    payer_id = request.GET.get('PayerID')

    paypalrestsdk.configure({
        "mode": settings.PAYPAL_MODE,
        "client_id": settings.PAYPAL_CLIENT_ID,
        "client_secret": settings.PAYPAL_CLIENT_SECRET
    })

    # Find the payment
    payment = paypalrestsdk.Payment.find(payment_id)

    if payment.execute({"payer_id": payer_id}):
        # ✅ Payment success — now extract useful info
        payer_info = payment.payer.payer_info
        transactions = payment.transactions[0]

        # Example details
        user_email = payer_info.email
        full_name = f"{payer_info.first_name} {payer_info.last_name}"
        transaction_id = transactions.related_resources[0].sale.id
        total_amount = transactions.amount.total
        currency = transactions.amount.currency
        description = transactions.description
        
        # paidid=str(uuid.uuid4().hex[:5]).upper()
        

        # Optional: Save to database
        PaymentRecord.objects.create(
            user=request.user,
            transaction_id=transaction_id,
            email=user_email,
            total_amount=total_amount,
            currency=currency,
            description=description,
            paid=True
        )

        context = {
            "success": True,
            "user_email": user_email,
            "full_name": full_name,
            "transaction_id": transaction_id,
            "amount": total_amount,
            "currency": currency,
            "description": description,
        }
        
        mycart=Cart.objects.filter(users=request.user).delete()

        return render(request, "pages/payment_success.html", context)

    else:
        print(payment.error)
        return render(request, "pages/payment_error.html", {"error": payment.error})
    
def cancel_payment(request):
    return HttpResponse("🚫 Payment was cancelled.")
