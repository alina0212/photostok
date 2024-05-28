from django.shortcuts import render
from product.models import Product


def main(request):
    all_products = Product.objects.all()

    return render(request, 'index_content.html',{'all_products': all_products})
