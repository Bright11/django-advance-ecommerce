from django.urls import path 

from . import views

app_name='commapp'

urlpatterns = [
    path('wishlist/<int:pk>/',views.wishlist.as_view(),name='wishlist'),
    path('details/<int:pdetails>/',views.details.as_view(),name='details'),
    path('getcategory/<int:category>/',views.getcategory.as_view(),name='getcategory'),
	path('',views.index.as_view(),name='index')
]
