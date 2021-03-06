"""sendy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from stores import views as store_views
from consumers import views as consumer_views
from products import views as product_views
from users import views as user_views
from logs import views as log_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stores/', store_views.index),
    path('login/', store_views.login),
    path('orm/',store_views.orm),
    path('get_full_soretname',store_views.get_full_storename),
    path('change_short_storename',store_views.change_short_storename),
    
]
