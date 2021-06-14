from django.urls import path
from .views import *
urlpatterns = [
    path('add/upload/',addachievementview,name='addachievementpage'),
    path('add/',addachievement),
    path('',homepageview)

]