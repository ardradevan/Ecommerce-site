from django.urls import path

from django.conf import settings
from .import views
from django.conf.urls.static import static
from store.controller import authview,cart,checkout
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.index,name="index"),
    path('product/',views.collections,name='products'),
    path('product/<str:slug>',views.collectionsview,name='collections'),
    path('product/<str:cate_slug>/<str:prod_slug>',views.productview,name='productview'),
    
    path('product-list',views.productListAjax),
    path('searchproduct',views.searchproduct,name="searchproduct"),
    
    path('register/',authview.register,name="register"),
    path('login/',authview.loginpage,name="loginpage"),
    path('logout/',authview.logoutpage,name="logout"),
    
    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    
    path('add-to-cart',cart.addtocart,name="addtocart"),
    path('cart',cart.viewcart,name="cart"),
    path('update-cart',cart.updatecart,name="updatecart"),
    path('delete-cart-item',cart.deletecartitem,name="deletecartitem"),
    
    path('checkout',checkout.index,name="checkout"),
    path('placeorder',checkout.placeorder,name="placeorder"),
    ]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)