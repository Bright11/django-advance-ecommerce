from django.urls import path 
from . import views
from django.contrib.auth import views as auth_views
from .forms import LoginForm
app_name="adminapp"
urlpatterns = [
    # path('uploadproduct',views.uploadproduct,name="uploadproduct"),
    path('addproduct/',views.addproduct.as_view(),name="addproduct"),
    path('logoutuser/',views.logoutuser,name="logoutuser"),
    path('login/',auth_views.LoginView.as_view(template_name='pages/login.html',authentication_form=LoginForm),name="login"),
     path('registeruser/',views.registeruser.as_view(),name="registeruser"),
    path('adminsubcats/',views.adminsubcats.as_view(),name="adminsubcats"),
	path('adminaddcat/',views.adminaddcat.as_view(),name='adminaddcat')
]
