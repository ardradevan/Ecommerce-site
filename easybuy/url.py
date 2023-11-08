from django.urls import path

from django.conf import settings
from .import views
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name="index"),
    path('product/',views.collections,name='products'),
    path('product/<str:slug>',views.collectionsview,name='collections'),
    path('product/<str:cate_slug>/<str:prod_slug>',views.productview,name='productview')
   
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)