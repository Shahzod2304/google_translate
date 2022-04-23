from django.urls import path
from .views import *

urlpatterns = [
    path('', Home, name='home'),
    path('about/', About, name='about'),
    path('contactus/', ContactUs, name='contactus'),
    path('translated/', Translated, name='translated'),
    
]