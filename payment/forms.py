from django import forms
from .models import Payment

class DateInput(forms.DateInput):
    input_type = 'date'

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'
        exclude = ('user', )
        widgets = {
            'date': DateInput(),
        }

    field_order = ["value", "source", "date"]
