from django.urls import path 

from . import views

app_name='commapp'

urlpatterns = [
    path('deletewishlist/<int:pk>/',views.deletewishlist.as_view(),name='deletewishlist'),
    path('deletecart/<int:pk>/',views.deletecart.as_view(),name='deletecart'),
    path('mycart/',views.mycart.as_view(),name="mycart"),
    path('addtocart/<int:cartid>/',views.addtocart.as_view(),name='addtocart'),
    path('mywishlist',views.mywishlist.as_view(),name='mywishlist'),
    path('wishlist/<int:pk>/',views.wishlist.as_view(),name='wishlist'),
    path('details/<int:pdetails>/',views.details.as_view(),name='details'),
    path('getcategory/<int:category>/',views.getcategory.as_view(),name='getcategory'),
	path('',views.index.as_view(),name='index')
]
