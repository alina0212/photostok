from django.db import models
from django.core.validators import RegexValidator


class Checkout(models.Model):
    phone_regex = RegexValidator(regex=r'\(+380)?\d{9,15}',
                                 message="Wrong phone number format. '+380....' up to 15 characters")
    phone_regex = RegexValidator(regex=r'^\+380\d{9}$',
                                 message="Wrong phone number format. '+380....'")
    f_name = models.CharField(max_length=20)
    l_name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=50)
    company_name = models.CharField(max_length=50, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20, validators=[phone_regex])
    image_ids = models.TextField(default='')
    image_ids = models.CharField(max_length=255)

    def __str__(self):
        return self.email
