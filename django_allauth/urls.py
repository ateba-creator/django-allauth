
from django.contrib import admin
from django.urls import path,include
import Mainapp.urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('home/',Mainapp.views.home,name='home'),
    path('',Mainapp.views.index,name='index')
]
