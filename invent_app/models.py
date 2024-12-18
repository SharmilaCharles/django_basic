from ast import mod
from django.db import models

class Products(models.Model):
    product_name = models.CharField(max_length=200, null=True)
    product_code = models.CharField(max_length=100, null=True)
    price = models.FloatField(default=0)
    gst = models.IntegerField(default=0)
    is_food_product = models.BooleanField(default=False)
    picture = models.ImageField(null=True,upload_to='images/')

    def __str__(self):
        return self.product_name 

