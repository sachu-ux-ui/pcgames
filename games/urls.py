from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.index, name='home'),
    path('add_products/',views.add_products,name='add_products'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('profile/',views.profile,name='profile'),
    path('editprofile/',views.editprofile,name='editprofile'),
    path('userlist/',views.userlist,name='userlist'),
    path('deleteuser/<int:id>/',views.deleteuser,name='deleteuser'),
    path('userproductlist/',views.userproductlist,name='userproductlist'),
    path('delete_cart/<int:id>/', views.delete_cart, name='delete_cart'),
    path('add_to_wishlist/<int:id>/', views.add_to_wishlist, name='add_to_wishlist'), 
    path('viewwishlist/', views.viewwishlist, name='viewwishlist'),
    path('productlist/', views.product_list, name='product_list'),
    path('add_to_cart/<int:id>/', views.add_to_cart, name='add_to_cart'),
    path('edit/<int:id>/', views.edit_product, name='edit_product'),
    path('delete/<int:id>/', views.delete_product, name='delete_product'),
    path('cart_list/',views.cart_list,name='cart_list'),
]