from django.shortcuts import render
from .models import Category
from product.models import Product


# Define the 'shop' view function with the request object as its argument.
def shop(request):
    # Retrieve all category records from the database.
    categories = Category.objects.all()

    # Retrieve all product records from the database where 'is_visible' is True.
    products = Product.objects.filter(is_visible=True)

    # Attempt to get the 'category' value from the URL query parameters (e.g., ?category=slug).
    selected_category_slug = request.GET.get('category', None)

    # Check if a category slug was provided in the URL query parameters.
    if selected_category_slug:
        # If a slug is provided, retrieve the first matching Category object.
        selected_category = Category.objects.filter(slug=selected_category_slug).first()

        # Filter products to only include those that belong to the selected category.
        products = products.filter(category=selected_category)

        # Update the 'categories_choice' to include only the selected category.
        categories_choice = [selected_category]
    else:
        # If no category slug is provided, default to the first category in the list.
        categories_choice = [categories.first()] if categories else []

    # Render the 'shop_content.html' template, passing in the categories, products,
    # and selected category context to be used in the template.
    return render(request, 'shop_content.html', context={
        'categories': categories,
        'products': products,
        'categories_choice': categories_choice,
    })
