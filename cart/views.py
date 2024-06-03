from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart, CartItem, Product
from django.contrib.sessions.models import Session
from django.http import HttpRequest, HttpResponse


def cart(request: HttpRequest):
    if not request.session.session_key:
        request.session.create()

    session_key = request.session.session_key
    session = get_object_or_404(Session, session_key=session_key)
    cart, created = Cart.objects.get_or_create(session=session)

    cart_items = CartItem.objects.filter(cart=cart)
    total_price = cart.total_cost

    return render(request, 'cart_content.html', {'cart_items': cart_items,
                                                 'total_price': total_price})


def add_to_cart(request: HttpRequest, product_id):
    product = get_object_or_404(Product, id=product_id)

    if not request.session.session_key:
        request.session.create()

    session_key = request.session.session_key
    session = get_object_or_404(Session, session_key=session_key)
    cart, created = Cart.objects.get_or_create(session=session)
    CartItem.objects.get_or_create(cart=cart, product=product)
    cart.calculate_price()
    return HttpResponse(status=204)



def remove_from_cart(request: HttpRequest, product_id):
    product = get_object_or_404(Product, id=product_id)

    if not request.session.session_key:
        request.session.create()

    session_key = request.session.session_key
    session = get_object_or_404(Session, session_key=session_key)
    cart = get_object_or_404(Cart, session=session)

    cart_item = get_object_or_404(CartItem, cart=cart, product=product)
    cart_item.delete()

    cart.calculate_price()

    return redirect('cart')
