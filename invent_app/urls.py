from django.urls import URLPattern, path
from .views import * 


urlpatterns = [
    path('', Homepage),
    path('about/',AboutPage),
    path('contact/',ContactPage),
    path('services/',ServicePage),

    # path('products_add/',Products_add),
    # path('allproducts/',AllProducts),
    # path('deleteproduct/<int:id>/',DeleteProduct,name = 'product_delete'),
    # path('updateproduct/<int:id>/',UpdateProduct,name = 'product_update'),

    path('products_add/',Productadd_view.as_view()),
    path('allproducts/',ProductListView.as_view()),
    path('deleteproduct/<int:id>/',ProductDeleteView.as_view(),name = 'product_delete'),
    path('updateproduct/<int:id>/',ProductUpdateView.as_view(),name = 'product_update'),
    
]