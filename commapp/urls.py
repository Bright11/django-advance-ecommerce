from django.urls import path 

from . import views

app_name='commapp'

urlpatterns = [
	path('',views.index.as_view(),name='index')
]
