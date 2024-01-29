from django.contrib import admin
from django.urls import path
from hello import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('about/', views.about),
    path('about2/', views.about2),
    path('about3/', views.about3),
# path('index/comp/1', comp1, name='comp1'),
]
