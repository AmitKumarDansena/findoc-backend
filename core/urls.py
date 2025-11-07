from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ipo-proxy/', views.ipo_proxy, name='ipo_proxy'),
]
