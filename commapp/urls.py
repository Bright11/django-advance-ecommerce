from django.urls import path 

from . import views

app_name='commapp'

urlpatterns = [
    path('getcategory/<int:category>/',views.getcategory.as_view(),name='getcategory'),
	path('',views.index.as_view(),name='index')
]
