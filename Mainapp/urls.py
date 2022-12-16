
from django.contrib import admin
from django.urls import path,include
from Mainapp.views import *

urlpatterns = [
    path('home/',home,name='home')
]
