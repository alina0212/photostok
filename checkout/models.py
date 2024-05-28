from django.db import models
from django.core.validators import RegexValidator


class Checkout(models.Model):
    phone_regex = RegexValidator(regex=r'^\+380\d{9}$',
                                 message="Phone number must be entered in the format: '+380xxxxxxxxx'. Up to 12 "
                                         "digits allowed.")

    f_name = models.CharField(max_length=20)
    l_name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=50)
    company_name = models.CharField(max_length=50, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20, validators=[phone_regex])
    image_ids = models.TextField(default='')

    def __str__(self):
        return self.f_name
