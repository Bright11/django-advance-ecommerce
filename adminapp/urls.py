from django.urls import path 
from . import views
from . import product
from django.contrib.auth import views as auth_views

app_name="adminapp"
urlpatterns = [
    # path('uploadproduct',views.uploadproduct,name="uploadproduct"),
    path('addproduct/',product.addproduct.as_view(),name="addproduct"),
    # path('adminsubcats/',views.adminsubcats.as_view(),name="adminsubcats"),
	path('adminaddcat/',views.adminaddcat.as_view(),name='adminaddcat'),
    path("updateproduct/<int:pk>/",product.updateproduct.as_view(), name='updateproduct'),
    path("viewproduct/",product.getallproduct.as_view(),name='viewproduct'),
    path("deletepro/<int:pk>/",product.deleteview.as_view(),name='deletepro'),
    # path("viewcategory/",views.viewcategory.as_view(), name='viewcategory'),
    path("update_category/<int:pk>/",views.updatecategory.as_view(),name='update_category'),
    path("deletecategory/<int:pk>/",views.deletecategory.as_view(), name='deletecategory'),
    path("viewsubcategory/",views.subcategory.as_view(), name='viewsubcategory'),
    path('updatesubcategory/<int:pk>/',views.updatesubcategory.as_view(), name='updatesubcategory'),
    path("deletesubcategory/<int:pk>/",views.deletesubcategory.as_view(), name="deletesubcategory"),
    # path("updatecategory/<int:pk/",views.updatecategory.as_view(), name='updatecategory')
]
