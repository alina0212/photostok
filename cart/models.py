from django.db import models
from django.contrib.sessions.models import Session
from product.models import Product
from decimal import Decimal
from django.db.models import Sum


class Cart(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE, related_name="cart")
    created_at = models.DateTimeField(auto_now_add=True)
    total_cost = models.DecimalField(max_digits=100, decimal_places=2, default=Decimal('0.00'))

    def calculate_price(self):
        total = self.cart_items.aggregate(total=Sum('product__price'))['total']
        if total is None:
            total = Decimal('0.00')
        total_price = round(total, 2)
        self.total_cost = total_price
        self.save()

    # def add_to_cart(self, product):
    #     cart_item, created = CartItem.objects.get_or_create(cart=self, product=product)
    #     if created:
    #         self.calculate_price()
    #
    # def remove_from_cart(self, product):
    #     try:
    #         cart_item = CartItem.objects.get(cart=self, product=product)
    #         cart_item.delete()
    #         self.calculate_price()
    #     except CartItem.DoesNotExist:
    #         pass


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='cart_items', on_delete=models.CASCADE)
    # product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
