from django.shortcuts import render
from .models import Category
from product.models import Product
from .forms import PriceFilterForm


def shop(request):
    categories = Category.objects.all()
    products = Product.objects.filter(is_visible=True)
    form = PriceFilterForm(request.GET or None)
    all_products = Product.objects.filter(is_visible=True)
    total_products = all_products.count()

    print("Initial products count:", products.count())  # Debugging line

    if form.is_valid():
        print("Form is valid")  # Debugging line
        min_price = form.cleaned_data.get('min_price')
        max_price = form.cleaned_data.get('max_price')
        if min_price is not None:
            products = products.filter(price__gte=min_price)
        if max_price is not None:
            products = products.filter(price__lte=max_price)
        print("Filtered products count:", products.count())  # Debugging line
    else:
        print("Form is not valid", form.errors)  # Debugging line

    selected_category_slug = request.GET.get('category', None)
    if selected_category_slug:
        selected_category = Category.objects.filter(slug=selected_category_slug).first()
        products = products.filter(category=selected_category)
        categories_choice = [selected_category]
    else:
        categories_choice = [categories.first()] if categories else []

    displayed_products_count = products.count()  # after filter

    return render(request, 'shop_content.html', {
        'categories': categories,
        'products': products,
        'categories_choice': categories_choice,
        'form': form,
        'total_products': total_products,
        'displayed_products_count': displayed_products_count
    })
