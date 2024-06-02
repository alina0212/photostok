from django.test import RequestFactory
from django.contrib.sessions.middleware import SessionMiddleware
from django.urls import reverse
import pytest
from product.models import Product
from product.models import Category
from cart.models import Cart, CartItem
from cart.views import cart, add_to_cart, remove_from_cart

@pytest.fixture
def rf():
    return RequestFactory()

@pytest.fixture
def session_middleware():
    return SessionMiddleware(lambda request: None)

@pytest.mark.django_db
def test_cart_view(rf, session_middleware):
    request = rf.get('/cart/')
    session_middleware.process_request(request)
    request.session.save()
    response = cart(request)
    assert response.status_code == 200

@pytest.mark.django_db
def test_add_to_cart_view(rf, session_middleware):
    category = Category.objects.create(name='Test Category')
    product = Product.objects.create(name='Test Product', price=10, category=category)
    request = rf.post(reverse('add_to_cart', args=[product.id]))
    session_middleware.process_request(request)
    request.session.save()
    response = add_to_cart(request, product.id)
    assert response.status_code == 204

@pytest.mark.django_db
def test_remove_from_cart_view(rf, session_middleware):
    category = Category.objects.create(name='Test Category')
    product = Product.objects.create(name='Test Product', price=10, category=category)
    
    # Setup request and session
    request = rf.post(reverse('remove_from_cart', args=[product.id]))
    session_middleware.process_request(request)
    request.session.save()

    # Associate Cart with session
    cart = Cart.objects.create(session_id=request.session.session_key)
    CartItem.objects.create(cart=cart, product=product)

    response = remove_from_cart(request, product.id)
    assert response.url == '/cart/'