"""food_box URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from app_food_box.views import food_list, recipient_list, food_detail, recipient_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('foods/', food_list, name='food-list'),
    path('recipients/', recipient_list, name='recipient_list'),
    path('foods/<int:pk>/', food_detail, name='food-detail'),
    path('recipients/<int:bk>/', recipient_detail, name='recipient_detail'),

]
