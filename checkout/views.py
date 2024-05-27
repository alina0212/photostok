import os
import zipfile
from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.sessions.models import Session
from cart.models import Cart
from .forms import CheckoutForm


def checkout(request):
    session_key = request.session.session_key
    if not session_key:
        request.session.create()
        session_key = request.session.session_key

    session = Session.objects.get(session_key=session_key)
    cart, created = Cart.objects.get_or_create(session=session)
    cart.calculate_price()

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('checkout_process')
    else:
        form = CheckoutForm()

    context = {
        'total_price': cart.total_cost,
        'form': form,
        'cart': cart
    }
    return render(request, 'checkout_content.html', context)


def checkout_process(request):
    session_key = request.session.session_key
    session = Session.objects.get(session_key=session_key)
    cart, created = Cart.objects.get_or_create(session=session)

    zip_subdir = "cart_images"
    zip_filename = f"{zip_subdir}.zip"

    response = HttpResponse(content_type="application/zip")
    response['Content-Disposition'] = f'attachment; filename={zip_filename}'

    with zipfile.ZipFile(response, "w") as zf:
        for item in cart.cart_items.all():
            product = item.product
            image_path = os.path.join(settings.MEDIA_ROOT, product.image.path)
            zf.write(image_path, os.path.join(zip_subdir, os.path.basename(image_path)))

    cart.cart_items.all().delete()
    cart.calculate_price()

    return response


