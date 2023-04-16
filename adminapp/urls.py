from django.urls import path 
from . import views

app_name="adminapp"
urlpatterns = [
	path('adminaddcat/',views.adminaddcat.as_view(),name='adminaddcat')
]
