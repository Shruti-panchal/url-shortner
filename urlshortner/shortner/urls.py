from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.index, name= 'index'),
    path('final', views.final, name='final'),
    path('<str:pk>', views.go, name='go')

]