from django.contrib import admin
from .models import Product


# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'price', 'category', 'sort', 'is_visible')
    list_filter = ('name', 'category', 'price', 'is_visible')
    list_editable = ('is_visible', 'sort', 'name', 'price')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('sort', 'name')  # Сортування за полем sort, потім за полем name


