import pytest
from django.urls import reverse
from shop.models import Category
from product.models import Product
from django.core.files.uploadedfile import SimpleUploadedFile


@pytest.fixture
def setup_data(db):
    category1 = Category.objects.create(name="Category 1", slug="category-1")
    category2 = Category.objects.create(name="Category 2", slug="category-2")
    image = SimpleUploadedFile(name='test_image.jpg', content=b'', content_type='image/jpeg')
    product1 = Product.objects.create(name="Product 1", price=50, is_visible=True, category=category1, image=image)
    product2 = Product.objects.create(name="Product 2", price=150, is_visible=True, category=category1, image=image)
    product3 = Product.objects.create(name="Product 3", price=250, is_visible=True, category=category2, image=image)
    product4 = Product.objects.create(name="Product 4", price=350, is_visible=True, category=category2, image=image)
    return category1, category2, product1, product2, product3, product4


@pytest.mark.django_db
def test_filter_by_category(client, setup_data):
    category1, category2, product1, product2, product3, product4 = setup_data

    # Використовуємо slug категорії для фільтрації
    url = reverse('shop_html')  # Переконайтеся, що це вірний URL для вашої функції shop
    response = client.get(url, {'category': category1.slug})
    assert response.status_code == 200

    content = response.content.decode()

    # Переконуємося, що вміст містить продукти тільки з категорії 1
    assert "Product 1" in content
    assert "Product 2" in content
    # Переконуємося, що продукти з категорії 2 не відображаються
    assert "Product 3" not in content
    assert "Product 4" not in content


@pytest.mark.django_db
def test_filter_by_min_price(client, setup_data):
    category1, category2, product1, product2, product3, product4 = setup_data

    # Використовуємо min_price для фільтрації
    url = reverse('shop_html')  # Переконайтеся, що це вірний URL для вашої функції shop
    response = client.get(url, {'min_price': 100})
    assert response.status_code == 200

    content = response.content.decode()
    print(content)
    # Переконуємося, що вміст містить продукти з ціною вище або рівною 100
    assert "Product 2" in content
    assert "Product 3" in content
    assert "Product 4" in content
    # Переконуємося, що продукти з ціною нижче 100 не відображаються
    assert "Product 1" not in content
