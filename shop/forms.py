from django import forms


class PriceFilterForm(forms.Form):
    min_price = forms.DecimalField(min_value=0, max_digits=10, decimal_places=2, required=False)
    max_price = forms.DecimalField(min_value=0, max_digits=100, decimal_places=2, required=False)
