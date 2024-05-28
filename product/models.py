from django.db import models
from shop.models import Category


class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=50)
    description = models.TextField(help_text="Вкажіть розмір, вагу та інші характеристики товару")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    image = models.ImageField(upload_to='products/')
    is_visible = models.BooleanField(default=True)
    sort = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('sort', 'name')
