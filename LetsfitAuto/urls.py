from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name="home"),
    path("index",views.index),
    path("customers",views.customers, name="customers"),    
    path("products",views.products,name="products"),    
]
