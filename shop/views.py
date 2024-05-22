from django.shortcuts import render
from .models import Category
from product.models import Product


def shop(request):
    categories = Category.objects.all()
    products = Product.objects.filter(is_visible=True)
    selected_category_slug = request.GET.get('category', None)

    if selected_category_slug:
        selected_category = Category.objects.filter(slug=selected_category_slug).first()
        products = products.filter(category=selected_category)
        categories_choice = [selected_category]
    else:
        categories_choice = [categories.first()] if categories else []

    return render(request, 'shop_content.html', context={
        'categories': categories,
        'products': products,
        'categories_choice': categories_choice,
    })
