from django.test import RequestFactory
from django.contrib.sessions.middleware import SessionMiddleware
from django.urls import reverse
import pytest
from product.models import Product
from cart.models import Cart, CartItem
from cart.views import cart, add_to_cart, remove_from_cart

@pytest.fixture
def rf():
    return RequestFactory()

@pytest.mark.django_db
def test_cart_view(rf):
    request = rf.get('/cart/')
    middleware = SessionMiddleware()
    middleware.process_request(request)
    request.session.save()
    response = cart(request)
    assert response.status_code == 200

@pytest.mark.django_db
def test_add_to_cart_view(rf):
    product = Product.objects.create(name='Test Product', price=10)
    request = rf.post(reverse('add_to_cart', args=[product.id]))
    middleware = SessionMiddleware()
    middleware.process_request(request)
    request.session.save()
    response = add_to_cart(request, product.id)
    assert response.status_code == 204

@pytest.mark.django_db
def test_remove_from_cart_view(rf):
    product = Product.objects.create(name='Test Product', price=10)
    cart = Cart.objects.create()
    cart_item = CartItem.objects.create(cart=cart, product=product)
    request = rf.post(reverse('remove_from_cart', args=[product.id]))
    middleware = SessionMiddleware()
    middleware.process_request(request)
    request.session.save()
    response = remove_from_cart(request, product.id)
    assert response.url == '/cart/'
