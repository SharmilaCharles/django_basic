from django.urls import path, include
from .views import * 

urlpatterns = [
    path('customer_add/',Customer_add,name='customer_add'),
    path('allcustomers/',AllCustomers,name='all_customers'),
    path('deletecustomer/<int:id>/',DeleteCustomer,name = 'customer_delete'),
    path('updatecustomer/<int:id>/',UpdateCustomer,name = 'customer_update'),

    path('vieworders/',OrdersView),
    path('addorders/',OrdersAdd),
    path('deleteorder/<int:id>/',DeleteOrder,name = 'order_delete'),
    path('updateorder/<int:id>/',UpdateOrder,name = 'order_update'),
]

