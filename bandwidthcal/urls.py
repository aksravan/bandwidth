from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<str:device>/', views.device, name='device'),
    path('<str:devicename>/add/', views.add, name='add'),
    path('result/', views.result, name='result'),
    path('reset/', views.reset, name='reset'),
]
