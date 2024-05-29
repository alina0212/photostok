import pytest
from django.core.files.uploadedfile import SimpleUploadedFile
from shop.models import Category
from product.models import Product
from decimal import Decimal


@pytest.fixture
def category(db):
    return Category.objects.create(name="Photography", slug="photography")


@pytest.mark.parametrize("name, slug, description, price, is_visible, sort, image_content", [
    ("Landscape Photo", "landscape-photo", "Beautiful landscape photo of mountains", Decimal('150.00'), True, 10,
     b'fake landscape data'),
    (
    "City Nightlife Photo", "city-nightlife", "Vibrant nightlife of the city captured in this photo", Decimal('200.00'),
    True, 20, b'fake city nightlife data'),
    ("Portrait Photo", "portrait-photo", "Professional portrait photo with blurred background", Decimal('175.00'), True,
     30, b'fake portrait data')
])
@pytest.mark.django_db
def test_create_photo_product(category, name, slug, description, price, is_visible, sort, image_content):
    image = SimpleUploadedFile(name=f'{slug}.jpg', content=image_content, content_type='image/jpeg')
    product = Product.objects.create(
        name=name,
        slug=slug,
        description=description,
        price=price,
        category=category,
        image=image,
        is_visible=is_visible,
        sort=sort
    )

    assert product.name == name
    assert product.slug == slug
    assert product.description == description
    assert product.price == price
    assert product.is_visible == is_visible
    assert product.sort == sort
    assert product.category == category
    assert f'products/{slug}.jpg' in product.image.name  # Виправлена перевірка шляху файлу зображення

    retrieved_product = Product.objects.get(id=product.id)
    assert retrieved_product.name == name
    assert retrieved_product.slug == slug
    assert retrieved_product.description == description
    assert retrieved_product.price == price
    assert retrieved_product.is_visible == is_visible
    assert retrieved_product.sort == sort
