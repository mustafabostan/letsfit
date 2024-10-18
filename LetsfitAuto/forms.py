from django import forms
from .models import Customer
from django.forms import TextInput

class customerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ["name","surname","mobile_number","status"]        
        widgets = {
            'name': TextInput(attrs={
                'class':"form-control"
            }),
            'surname': TextInput(attrs={
                'class':"form-control"
            }),
            'mobile_number': TextInput(attrs={
                'class':"form-control"
            }),            
        }