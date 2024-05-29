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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from main.views import main
from cart.views import cart, add_to_cart, remove_from_cart
from checkout.views import checkout, create_zip
from photostok import settings
from shop.views import shop, search_view
from product.views import Product, product_detail


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main, name='main'),
    path('index.html', main, name='main_html'),

    path('cart/', cart, name='cart'),
    path('cart.html', cart, name='cart_html'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:product_id>/', remove_from_cart, name='remove_from_cart'),

    path('checkout/', checkout, name='checkout'),
    path('checkout.html', checkout, name='checkout_html'),
    path('create_zip/', create_zip, name='create_zip'),

    path('shop/', shop, name='shop'),
    path('shop.html', shop, name='shop_html'),
    path('product/', product_detail, name='product_detail'),
    path('search/', search_view, name='search_view'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
