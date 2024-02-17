from django.contrib import admin
from django.urls import path, re_path
from shop import views
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static
#
#
urlpatterns = [
     path('admin/', admin.site.urls),
     path('testcar', views.testcar),
#Сайты========================================================================================================================================================================
     path('main/', views.index, name='main'),
     path('delivery', views.page_dostavka, name='delivery'),
     path('catalog/', views.catalog, name='catalog'),
     path('order/', views.order2, name='order'),
#Каталог товаров=================================================================================================================================================================================================
     path('catalog/televizory-i-cifrovoe-tv/', views.testcar, name='catalog/-tv'),
     # path('catalog/cold-storage/', views.cold_storage, name='catalog/cold-storage'),
     # path('catalog/noytbyki/', views.noytbyki, name='catalog/noytbyki'),
     # path('catalog/kofemashini/', views.kofemashini, name='catalog/kofemashini'),
     # path('catalog/proektori/', views.proektori, name='catalog/proektori'),
     # path('catalog/fleshki/', views.fleshki, name='catalog/fleshki'),
# Товары===========================================================================================================================================================================================
#      path('catalog/televizory-i-cifrovoe-tv/grunding65', views.televizor1, name='televizor1'),
]
#
# # включаем возможность обработки картинок
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)