from django.urls import path
# from .views import *
from . import views
from .forms import LoginForm
from django.contrib.auth import views as auth_views


app_name='authapp'

urlpatterns = [
     path('logoutuser/',views.logoutuser,name="logoutuser"),
    path('login/',auth_views.LoginView.as_view(template_name='pages/login.html',authentication_form=LoginForm),name="login"),
      path('registeruser/',views.registeruser.as_view(),name="registeruser"),
      path("deleteuser/", views.deleteview.as_view(), name='deleteuser')
]
