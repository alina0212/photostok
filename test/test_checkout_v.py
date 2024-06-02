import os
import tempfile
import zipfile
from django.test import RequestFactory, TestCase
from django.contrib.sessions.middleware import SessionMiddleware
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from decimal import Decimal
from shop.models import Category
from product.models import Product
from cart.models import Cart, CartItem
from checkout.views import checkout, create_zip
from checkout.forms import CheckoutForm

class CheckoutTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        category = Category.objects.create(name="Test Category", slug="test-category")
        self.product = Product.objects.create(name='Test Product', price=10, category=category)  

        self.cart = Cart.objects.create(session_id=self.client.session.session_key)
        self.cart_item = CartItem.objects.create(cart=self.cart, product=self.product)

    def test_checkout_view(self):
        request = self.factory.get('/checkout/')
        middleware = SessionMiddleware(lambda x: None)
        middleware.process_request(request)
        request.session.save()
        response = checkout(request)
        self.assertEqual(response.status_code, 200)

    def test_checkout_form_valid(self):
        request = self.factory.post('/checkout/', {
            'f_name': 'test',
            'l_name': 'test',
            'email': 'gg@gg.gg',
            'phone': '+380123456789',
            'image_ids': '1,2,3'
        })
        middleware = SessionMiddleware(lambda x: None)
        middleware.process_request(request)
        request.session.save()

        form = CheckoutForm(request.POST)
        self.assertTrue(form.is_valid())


class CreateZipTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        category = Category.objects.create(name="Test Category", slug="test-category")
        self.product = Product.objects.create(name='Test Product', price=10, category=category)  
        self.cart = Cart.objects.create(session_id=self.client.session.session_key)
        self.cart_item = CartItem.objects.create(cart=self.cart, product=self.product)

    def test_create_zip(self):
        request = self.factory.get(reverse('create_zip'))
        middleware = SessionMiddleware(lambda x: None)
        middleware.process_request(request)
        request.session.save()
        response = create_zip(request)
        self.assertEqual(response.status_code, 200)
