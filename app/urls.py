"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from store.views import create_item, get_items, create_employee, get_employees, get_customers, add_customer, get_orders, make_order, get_orders_details

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create_item', create_item, name='create_item'),
    path('get_items', get_items, name='get_items'),
    path('create_employee', create_employee, name='create_employee'),
    path('get_employees', get_employees, name='get_employees'),
    path('get_customers', get_customers, name='get_customers'),
    path('add_customer', add_customer, name='add_customer'),
    path('get_orders', get_orders, name='get_orders'),
    path('make_order', make_order, name='make_order'),
    path('get_orders_details', get_orders_details, name='get_orders_details'),
]
