from django.contrib import admin
from django.urls import path
from shop import views
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('comp1', views.test),
    path('comp2', views.test2),
    path('testcar', views.testcar),


    # path('about/', views.vse),
    # path('delivery/', views.about3),
    # path('order/', views.about3),
    # path('catalog/', views.about3),
    # path('catalog/televizory-i-cifrovoe-tv/', views.about3),
    # path('catalog/cold-storage/', views.about3),
    # path('catalog/noytbyki/', views.about3),
    # path('catalog/kofemashini/', views.about3),
    # path('catalog/proektori/', views.about3),
    # path('catalog/fleshki/', views.about3),



    # path('login/', views.about3),
    # path('index/comp/1', comp1, name='comp1'),
]

# включаем возможность обработки картинок
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
