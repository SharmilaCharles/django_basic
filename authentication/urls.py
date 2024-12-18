from django.urls import URLPattern, path
from .views import * 

urlpatterns  = [
    path('',Login),
    path("logout/",LogoutUser),
    path('signup/',Signup)
]