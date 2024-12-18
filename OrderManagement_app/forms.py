from dataclasses import field
from django import forms
from .models import Customer, Orders

class Customer_Form(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['customer_name', 'customer_since']  

        widgets = {
            'customer_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter customer name'
            }),
            'customer_since': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
        }

class Order_Form(forms.ModelForm):
    class Meta: 
        model = Orders
        fields =['customer_reference','product_reference','order_number','order_date','quantity']

        widgets = {
            'customer_reference': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Select customer Name'
            }),
            'product_reference': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Select Product Name'
            }),
            'order_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Order Number'
            }),
            'order_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'quantity': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter quantity'
            }),
        }