from django.shortcuts import render, redirect

import invent_app
from .models import *
from invent_app.models import Products
from .forms import Customer_Form, Order_Form
from django.contrib.auth.decorators import login_required

@login_required(login_url = '/')

def Customer_add(request):
    if request.method == 'POST':
        customer_form_variable = Customer_Form(request.POST)
        if customer_form_variable.is_valid():
            customer_form_variable.save()
            print("Customer saved successfully!")
            return redirect('/order/allcustomers/')  # Redirect to avoid duplicate submissions
        else:
            print(customer_form_variable.errors)  # Debug invalid form data

    context = {
        'customer_add_con': Customer_Form()
    }
    return render(request, 'customer_add.html', context)

@login_required(login_url = '/')
def AllCustomers(request):
    all_customers = Customer.objects.all()
    return render(request, 'allcustomers.html', {'all_customers': all_customers})

@login_required(login_url = '/')
def DeleteCustomer(request, id):
    selected_product = Customer.objects.get(id = id)
    selected_product.delete()
    return redirect('/order/allcustomers/')

@login_required(login_url = '/')
def UpdateCustomer(request, id):
    selected_product = Customer.objects.get(id = id)
    context = {
        'customer_form_variable' : Customer_Form (instance=selected_product)

    }
    if request.method == 'POST':
        customer_form_variable = Customer_Form(request.POST, instance =selected_product )

        if customer_form_variable.is_valid():
            customer_form_variable.save()
            return redirect('/order/allcustomers/')

    return render (request,'customer_update.html',context)

@login_required(login_url = '/')
def OrdersAdd (request):
    context = {
        'order_form' : Order_Form()
    }
    if request.method == 'POST':
        selected_product = Products.objects.get(id=request.POST['product_reference'])
        amount = float (selected_product.price) * float (request.POST['quantity'])
        gst_amount = (amount*selected_product.gst)/100
        bill_amount = amount + gst_amount

        new_order = Orders (customer_reference_id = request.POST['customer_reference'],
                            product_reference_id = request.POST['product_reference'],
                            order_number = request.POST['order_number'],
                            order_date = request.POST['order_date'],
                            quantity = request.POST['quantity'],
                            amount = amount,
                            gst_amount = gst_amount,
                            bill_amount = bill_amount
                            )
        new_order.save()
    
    return render(request, 'orders_add.html', context)

@login_required(login_url = '/')
def OrdersView(request):
    context = {
        'all_order' : Orders.objects.all()
    }
    return render (request, 'view_orders.html',context)

@login_required(login_url = '/')
def DeleteOrder(request, id):
    selected_product = Orders.objects.get(id = id)
    selected_product.delete()
    return redirect('/order/vieworders/')

@login_required(login_url = '/')
def UpdateOrder(request, id):
    selected_product = Orders.objects.get(id = id)
    context = {
        'order_form' : Order_Form (instance=selected_product)
    }
    if request.method == 'POST':
        selected_product = Products.objects.get(id=request.POST['product_reference'])
        amount = float (selected_product.price) * float (request.POST['quantity'])
        gst_amount = (amount*selected_product.gst)/100
        bill_amount = amount + gst_amount

        order_filter = Orders.objects.filter(id = id)

        order_filter.update(
                            customer_reference_id = request.POST['customer_reference'],
                            product_reference_id = request.POST['product_reference'],
                            order_number = request.POST['order_number'],
                            order_date = request.POST['order_date'],
                            quantity = request.POST['quantity'],
                            amount = amount,
                            gst_amount = gst_amount,
                            bill_amount = bill_amount
        )
        return redirect('/order/vieworders/')

        

    return render (request,'order_update.html',context)