import pytest
from django.core.exceptions import ValidationError
from checkout.models import Checkout

@pytest.mark.django_db
def test_valid_checkout():
    checkout = Checkout(
        f_name='test',
        l_name='test',
        email='gg@gg.gg',
        phone='+380123456789',
        image_ids='1,2,3'
    )
    checkout.full_clean()  

@pytest.mark.django_db
def test_invalid_checkout_phone():
    with pytest.raises(ValidationError) as e:
        checkout = Checkout(
            f_name='test',
            l_name='test',
            email='gg@gg.gg',
            phone='123456789', 
            image_ids='1,2,3'
        )
        checkout.full_clean()  

    assert 'Wrong phone number format' in str(e.value)

    

@pytest.mark.django_db
def test_string_representation():
    checkout = Checkout(
        f_name='test',
        l_name='test',
        email='gg@gg.gg',
        phone='+380123456789',
        image_ids='1,2,3'
    )
    assert str(checkout) == 'gg@gg.gg'
