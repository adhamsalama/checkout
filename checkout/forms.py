from django.forms import ModelForm
from .models import Item
from django import forms
from datetime import datetime

#class ItemForm(ModelForm):
#    class Meta:
#        model = Item
#        fields = ["name", "price", "quantity", "category", "date", "comment"]
#    #category = forms.CharField(required=False)
#    #date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', "value": datetime.now().strftime('%Y-%m-%d')}))
#    field_order=["name", "price", "quantity", "date", "category", "comment"]

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
    field_order=["name", "price", "quantity", "seller", "date", "category", "comment"]