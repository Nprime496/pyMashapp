from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home),
    path('read',views.read_csv,name='read'),
    path('sent',views.send_a_mail,name='send')
]