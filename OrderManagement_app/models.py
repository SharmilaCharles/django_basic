from django.db import models
from invent_app.models import Products

class Customer(models.Model):
    customer_name =models.CharField(max_length=100, null=True)
    customer_since = models.DateField(null=True)

    def __str__(self):
        return self.customer_name

class Orders(models.Model):
    customer_reference = models.ForeignKey(Customer, on_delete=models.CASCADE,null=True)
    product_reference = models.ForeignKey(Products,on_delete=models.SET_NULL,null=True)
    order_number = models.CharField(null=True,max_length=10)
    order_date = models.DateField(null=True)
    quantity = models.FloatField(default=0)
    amount=models.FloatField(default=0)
    gst_amount = models.FloatField(default=0)
    bill_amount = models.FloatField(default=0)

    def __str__(self):
        return self.order_number
    
