from fileinput import FileInput
from django.forms import ModelForm
from .models import *
from django.forms import ModelForm, TextInput, NumberInput, CheckboxInput,FileInput

class product_form(ModelForm):
    class Meta: 
        model = Products
        fields = "__all__"
        # fields = ['product_name','product_code', 'price', 'gst','is_food_product']
        
        widgets = {
            'product_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter product name'}),
            'product_code': TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter product code'}),
            'price': NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter price'}),
            'gst': NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter GST'}),
            'is_food_product  ': CheckboxInput(attrs={'class': 'form-check-input'}),
            'picture': FileInput(attrs={'class': 'form-control'}),
        }