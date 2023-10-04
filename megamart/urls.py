from django.contrib import admin
from django.urls import path, include
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('master/',views.Master,name='Master'),
    path('signup/',views.Signup,name='signup'),
    path('',views.Index,name='index'),
    path('accounts/',include('django.contrib.auth.urls')),

    #cart path
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),

    path('contact-us/',views.Contact, name='contact-us'),
    path('checkout/',views.CheckOut, name='checkout'),
    path('order/',views.Your_Order,name='order'),

     # product page
     path('product/',views.Product_page, name='product_page'),

     # product details
     path('product_detail/',views.Product_detail, name='product_detail'),

     #search result
     path('search/',views.Search,name='search'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
