from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.loginUser, name="login"),
    path('logout', views.logoutUser, name='logout'),
    path('mainPage', views.mainPage, name='mainPage'),
    path('form', views.form, name='form'),
    path('appointment', views.appointment, name='appointment'),
]