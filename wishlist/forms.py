from django.forms import ModelForm
from .models import Wishlist
from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'


class WishlistForm(forms.ModelForm):
    class Meta:
        model = Wishlist
        fields = '__all__'
        exclude = ('user', 'date')
        widgets = {
            'date': DateInput(),
        }
