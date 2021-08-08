"""ShopFantasy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Items.views import *


urlpatterns = [
    path('register/', register_request, name="register"),
    path('admin/', admin.site.urls),
    path('logout/', logout_request, name="logout"),
    path('login/', login_request, name="login"),
    path('', index),
    path('category/<id>/', category, name='category'),
    path('items/<id>/', items, name='items'),
    path('search/', get_queryset, name='search_results'),
]
