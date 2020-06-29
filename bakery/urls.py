from django.urls import path, include
from bakery import views

app_name="bakery"

urlpatterns = [

     path('', views.bakery1pageview.as_view()),
	 path('menu/', views.menupageview.as_view()),
	 path('about/', views.aboutpageview.as_view()),
	 path('products/', views.product_list),
     path('services/', views.servicespageview.as_view()),
     path('offer/', views.offerpageview.as_view()),
     path('blog/', views.blogpageview.as_view()),
     path('contacts/', views.contactspageview.as_view()),
	 path('order/', views.productlist),
	 path('insertcontact/', views.insertcontact),
	 path('insertorder/', views.insertorder),
	 
	 
 
     
]