from django.shortcuts import render
from .models import Category
from product.models import Product


# Create your views here.
def shop(request):
    categories = Category.objects.all()
    products = Product.objects.filter(is_visible=True)
    return render(request, 'shop_content.html', context={
        'categories': categories,
        'products': products,
        'categories_choise': [categories[0]],

    })
# Create your views here.
