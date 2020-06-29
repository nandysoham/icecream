# added manually
from django.contrib import admin
from django.urls import path, include
from home import views


urlpatterns = [
    path('',views.index, name='home'),
    path('services',views.services, name='services'),
    path('contact',views.contact, name='contact'),
    path('about',views.about, name='about'),
    path('login',views.ulogin, name='login'),
    path('logout',views.logout, name='logout'),
    path('userpage',views.userpage, name='userpage'),
    path('shop',views.shop, name='shop'),
    path('shop_prodpage/<int:id>',views.prodview, name='prodview')



]