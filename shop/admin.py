from django.contrib import admin
from .models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'sort', 'slug')
    list_editable = ('sort', 'name', 'slug')
    search_fields = ('name', 'sort')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('sort', 'name')  # Сортування за полем sort, потім за полем name