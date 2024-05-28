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
    return product1


@pytest.mark.django_db
def test_product_detail_redirect_if_no_product_id(client):
    url = reverse('product_detail')
    response = client.get(url)
    assert response.status_code == 302  # Check if there is a redirect
    assert response.url == reverse('main_html')  # Check if it redirects to the home page


@pytest.mark.django_db
def test_product_detail_page_renders_correctly(client, setup_data):
    product1 = setup_data
    url = reverse('product_detail')
    response = client.get(url, {'product_id': product1.id})
    assert response.status_code == 200  # Check if the page loads successfully
    assert 'product' in response.context  # Check if the context contains the product
    assert response.context['product'].name == product1.name  # Check if the correct product is passed


@pytest.mark.django_db
def test_product_detail_404_if_product_not_exists(client):
    non_existent_product_id = 999  # ID of a product that does not exist
    url = reverse('product_detail')
    response = client.get(url, {'product_id': non_existent_product_id})
    assert response.status_code == 404  # Check if it returns a 404 status
