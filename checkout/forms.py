from django.forms import ModelForm
from .models import Item
from django import forms
from datetime import datetime


class DateInput(forms.DateInput):
    input_type = 'date'

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
        exclude = ('user', 'category')
        widgets = {
            'date': DateInput(),
        }
    category = forms.CharField(required=False)
    field_order = ["name", "price", "quantity", "seller", "date", "category", "comment"]