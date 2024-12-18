from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def Homepage(request):
    context = {
        "name" : 'Jenson',
        "role" : 'admin',
        "age" : "15",
        "marks" : {
            'tamil' : 34,
            'English' : 45
        }
    }
    return render(request,'home.html',context)

def AboutPage(request):
    return render(request, 'about.html')

def ServicePage(request):
    return render(request,'services.html')

def ContactPage(request):
    return render(request, 'contact.html')

# def Products_add(request):
    context = {
        'product_add_con' : product_form()
    }
    if request.method == 'POST':
        product_form_variable = product_form(request.POST)

        if product_form_variable.is_valid(): 
            product_form_variable.save()

    return render(request,'products_add.html',context)

# def AllProducts(request):
#     all_products = Products.objects.all()
#     return render(request, 'products.html',{'all_products':all_products})

# def DeleteProduct(request, id):
#     selected_product = Products.objects.get(id = id)
#     selected_product.delete()

#     return redirect('/allproducts/')

# def UpdateProduct(request, id):
#     selected_product = Products.objects.get(id = id)
#     context = {
#         'product_form_variable' : product_form (instance=selected_product)

#     }
#     if request.method == 'POST':
#         product_form_variable = product_form(request.POST, instance =selected_product )

#         if product_form_variable.is_valid():
#             product_form_variable.save()
#             return redirect('/inventry/allproducts/')

#     return render (request,'update.html',context)

class Productadd_view(LoginRequiredMixin,View):
    login_url = '/'
    def get(self,request):
         context = {
        'product_add_con' : product_form()
    }
         return render(request,'products_add.html',context)
            

    def post(self,request):
        product_form_variable = product_form(request.POST,request.FILES)

        if product_form_variable.is_valid(): 
            product_form_variable.save()

            return redirect('/inventry/allproducts/')    

class ProductListView(LoginRequiredMixin,View):
    login_url = '/'
    def get(self, request):
        all_products = Products.objects.all()
        return render(request, 'products.html',{'all_products':all_products})

class ProductDeleteView(LoginRequiredMixin,View):
    login_url = '/'
    def get(self,request,id):
        selected_product = Products.objects.get(id = id)
        selected_product.delete()

        return redirect('/inventry/allproducts/')
    
class ProductUpdateView(LoginRequiredMixin,View):
    login_url = '/'
    def get(self, request,id):
         selected_product = Products.objects.get(id = id)
         context = {
            'product_form_variable' : product_form (instance=selected_product)

            }
         return render (request,'update.html',context)
    
    def post(self,request, id):
         selected_product = Products.objects.get(id = id)
         product_form_variable = product_form(request.POST, instance =selected_product )
         if product_form_variable.is_valid():
                product_form_variable.save()
                return redirect('/inventry/allproducts/')
