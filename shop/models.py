from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    sort = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('sort', 'name')  # Сортування за полем sort, потім за полем name