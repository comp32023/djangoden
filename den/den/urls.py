from django.contrib import admin
from django.urls import path
from shop import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('comp1', views.test),
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
