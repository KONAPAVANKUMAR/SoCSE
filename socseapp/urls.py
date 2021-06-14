from django.urls import path
from .views import *

urlpatterns = [
    path('',indexview,name = 'indexpageview'),
    path('logoutuser/',logoutuser,name = 'logoutuser'),

    
]