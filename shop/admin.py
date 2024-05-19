from django.contrib import admin
from .models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'sort')
    list_editable = ('sort','name')
    search_fields = ('name','sort')
    ordering = ('sort', 'name')  # Сортування за полем sort, потім за полем name