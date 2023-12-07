from django.urls import path

from django.conf import settings
from .import views
from django.conf.urls.static import static
from store.controller import authview,cart
urlpatterns = [
    path('',views.index,name="index"),
    path('product/',views.collections,name='products'),
    path('product/<str:slug>',views.collectionsview,name='collections'),
    path('product/<str:cate_slug>/<str:prod_slug>',views.productview,name='productview'),
    
    path('product-list',views.productListAjax),
    
    path('register/',authview.register,name="register"),
    path('login/',authview.loginpage,name="loginpage"),
    path('logout/',authview.logoutpage,name="logout"),
    
    path('add-to-cart',cart.addtocart,name="addtocart"),
    path('cart',cart.viewcart,name="cart"),
    path('update-cart',cart.updatecart,name="updatecart"),
    path('delete-cart-item',cart.deletecartitem,name="deletecartitem")
    ]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)