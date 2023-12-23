from django.urls import path 
from .views import *

urlpatterns = [
   
    path('', index, name='index'),
    path('contact_us/', contact_Us, name='contact_us'),
]
