"""
URL configuration for photostok project.

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
from main.views import main
from cart.views import cart
from checkout.views import checkout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main, name='main'),
    path('index.html', main, name='main_html'),
    path('cart/', cart, name='cart'),
    path('cart.html', cart, name='cart_html'),
    path('checkout/', checkout, name='checkout'),
    path('checkout.html', checkout, name='checkout_html'),

]
