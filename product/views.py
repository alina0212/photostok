from django.shortcuts import render, get_object_or_404, redirect
from .models import Product


def product_detail(request):
    product_id = request.GET.get('product_id', None)
    if product_id is None:
        return redirect('main_html')  # Redirect to home if no product_id is provided

    product = get_object_or_404(Product, pk=product_id)  # This correctly handles 404 if the product doesn't exist

    return render(request, 'product_content.html', {'product': product})
