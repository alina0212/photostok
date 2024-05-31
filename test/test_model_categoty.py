import pytest
from django.db.utils import IntegrityError
from shop.models import Category
from product.models import Product
from decimal import Decimal


@pytest.fixture
def create_category(db):
    def _create_category(name="Test Category", sort=0, slug="default-slug"):
        return Category.objects.create(name=name, sort=sort, slug=slug)

    return _create_category


@pytest.fixture
def create_product(db, create_category):
    def _create_product(name, slug, description, price, category, is_visible, sort):
        return Product.objects.create(
            name=name,
            slug=slug,
            description=description,
            price=Decimal(price),
            category=category,
            is_visible=is_visible,
            sort=sort
        )

    return _create_product


@pytest.mark.parametrize("name, sort, slug", [
    ("Test Category", 10, "test-category"),
    ("Another Category", 5, "another-category")
])
@pytest.mark.django_db
def test_create_category(create_category, name, sort, slug):
    category = create_category(name=name, sort=sort, slug=slug)
    assert category.name == name
    assert category.sort == sort
    assert category.slug == slug


@pytest.mark.django_db
def test_default_slug(create_category):
    category = create_category(name="Test Category No Slug", slug="default-slug")
    assert category.slug == "default-slug"


@pytest.mark.django_db
def test_category_ordering(create_category):
    category1 = create_category(name="Alpha Category", sort=2, slug="default-slug")
    category2 = create_category(name="Beta Category", sort=1, slug="default-slug2")
    categories = Category.objects.all()
    assert categories[0] == category2
    assert categories[1] == category1


@pytest.mark.django_db
def test_category_iteration(create_category, create_product):
    category = create_category(name="Test Category")
    product1 = create_product(name="Visible Product", slug="visible-product", description="Visible Product Description",
                              price='100.00', category=category, is_visible=True, sort=1)
    product2 = create_product(name="Hidden Product", slug="hidden-product", description="Hidden Product Description",
                              price='100.00', category=category, is_visible=False, sort=2)

    products = list(category)
    assert len(products) == 1
    assert products[0] == product1


@pytest.mark.django_db
def test_category_str(create_category):
    category = create_category(name="Test Category")
    assert str(category) == "Test Category"


@pytest.mark.django_db
def test_unique_slug(create_category):
    create_category(name="Unique Slug Category", slug="unique-slug")
    with pytest.raises(IntegrityError):
        create_category(name="Duplicate Slug Category", slug="unique-slug")
