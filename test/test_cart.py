import pytest
from django.contrib.sessions.models import Session
from django.utils import timezone
from datetime import timedelta
from django.db import IntegrityError
from django.test import RequestFactory
from decimal import Decimal
from shop.models import Category
from product.models import Product
from cart.models import Cart, CartItem


@pytest.fixture
def create_cart(db):
    # Create a session for the cart with timezone support
    expire_date = timezone.now() + timedelta(days=1)
    session = Session.objects.create(expire_date=expire_date)
    return Cart.objects.create(session=session)


@pytest.fixture
def create_product(db):
    # Create a product
    category = Category.objects.create(name="Test Category", slug="test-category")
    return Product.objects.create(name="Test Product", price=Decimal('10.00'), is_visible=True, category=category)


@pytest.mark.django_db
def test_cart_creation(create_cart):
    assert Cart.objects.count() == 1


@pytest.mark.django_db
def test_cart_total_cost_initial(create_cart):
    assert create_cart.total_cost == Decimal('0.00')


@pytest.mark.django_db
def test_cart_total_cost_after_adding_item(create_cart, create_product):
    cart = create_cart
    product = create_product
    cart_item = CartItem.objects.create(cart=cart, product=product)
    cart.calculate_price()
    assert cart.total_cost == product.price


@pytest.mark.django_db
def test_cart_total_cost_after_removing_item(create_cart, create_product):
    cart = create_cart
    product = create_product
    cart_item = CartItem.objects.create(cart=cart, product=product)
    cart.calculate_price()
    assert cart.total_cost == product.price
    cart_item.delete()
    cart.calculate_price()
    assert cart.total_cost == Decimal('0.00')


@pytest.mark.django_db
def test_cart_total_cost_with_multiple_items(create_cart, create_product):
    cart = create_cart
    product1 = create_product
    product2 = Product.objects.create(name="Second Product", price=Decimal('20.00'), is_visible=True, category=product1.category)
    CartItem.objects.create(cart=cart, product=product1)
    CartItem.objects.create(cart=cart, product=product2)
    cart.calculate_price()
    assert cart.total_cost == Decimal('30.00')


@pytest.mark.django_db
def test_cart_item_creation(create_cart, create_product):
    cart = create_cart
    product = create_product
    cart_item = CartItem.objects.create(cart=cart, product=product)
    assert CartItem.objects.count() == 1
    assert cart_item.product == product
    assert cart_item.cart == cart


@pytest.mark.django_db
def test_cart_item_deletion(create_cart, create_product):
    cart = create_cart
    product = create_product
    cart_item = CartItem.objects.create(cart=cart, product=product)
    assert CartItem.objects.count() == 1
    cart_item.delete()
    assert CartItem.objects.count() == 0
