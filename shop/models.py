from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    sort = models.IntegerField(default=0)
    slug = models.SlugField(max_length=50, unique=True, default='default-slug')

    def __iter__(self):
        for product in self.products.filter(is_visible=True):
            yield product

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('sort', 'name')  # sort first on sorting, then name
