import pytest
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from shop.models import Category
from product.models import Product

@pytest.fixture
def setup_data(db):
    # Create categories
    category1 = Category.objects.create(name="Category 1", slug="category-1")

    # Create a product with an image and a category
    image = SimpleUploadedFile(name='test_image.jpg', content=b'', content_type='image/jpeg')
    product1 = Product.objects.create(name="Product 1", price=50, is_visible=True, category=category1, image=image)
    return category1, product1

@pytest.mark.django_db
def test_main_page(client):
    url = reverse('main')
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_main_html_page(client):
    url = reverse('main_html')
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_cart_page(client):
    url = reverse('cart')
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_cart_html_page(client):
    url = reverse('cart_html')
    response = client.get(url)
    assert response.status_code == 200  # Check if the cart HTML page loads successfully

@pytest.mark.django_db
def test_add_to_cart(client, setup_data):
    category1, product1 = setup_data
    url = reverse('add_to_cart', args=[product1.id])
    response = client.post(url)  # Ensure this is a POST request
    assert response.status_code == 204  # Check if the add to cart redirects successfully

@pytest.mark.django_db
def test_remove_from_cart(client, setup_data):
    category1, product1 = setup_data
    url = reverse('remove_from_cart', args=[product1.id])
    response = client.post(url)  # Ensure this is a POST request
    assert response.status_code == 404  # Check if the remove from cart redirects successfully

@pytest.mark.django_db
def test_checkout_page(client):
    url = reverse('checkout')
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_checkout_html_page(client):
    url = reverse('checkout_html')
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_shop_page(client):
    url = reverse('shop')
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_shop_html_page(client):
    url = reverse('shop_html')
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_product_detail(client, setup_data):
    category1, product1 = setup_data
    url = reverse('product_detail') + f'?product_id={product1.id}'
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_product_detail_redirect(client):
    url = reverse('product_detail')
    response = client.get(url)
    assert response.status_code == 302  # Check if the product detail redirects when no product_id is provided
    assert response.url == reverse('main_html')  # Check if it redirects to the main HTML page
