from django import forms
from .models import Checkout


class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Checkout
        fields = ('f_name', 'l_name', 'company_name', 'email', 'phone')
        widgets = {
            'f_name': forms.TextInput(attrs={'class': 'form-control',
                                             'id': 'first_name',
                                             'value': '',
                                             'placeholder': 'First Name'}),
            'l_name': forms.TextInput(attrs={'class': 'form-control',
                                             'id': 'last_name',
                                             'value': '',
                                             'placeholder': 'Last Name'}),
            'company_name': forms.TextInput(attrs={'class': 'form-control',
                                                   'id': 'company',
                                                   'value': '',
                                                   'placeholder': 'Company Name (if you are)'}),
            'email': forms.EmailInput(attrs={'class': 'form-control',
                                             'id': 'email',
                                             'value': '',
                                             'placeholder': 'Email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control',
                                            'id': 'phone_number',
                                            'value': '',
                                            'placeholder': 'Phone No',
                                            'min': '0'})

        }

        labels = {
            'f_name': 'First Name',
            'l_name': 'Last Name',
            'company_name': 'Company Name (if you are)',
            'email': 'Email',
            'phone': 'Phone No'
        }

        help_texts = {
            'phone': 'Enter a phone number in the format +380XXXXXXXXX'
        }

        error_messages = {
            'f_name': {'required': 'This field is required'},
            'l_name': {'required': 'This field is required'},
            'email': {'required': 'This field is required'},
            'phone': {'required': 'This field is required'},
        }
