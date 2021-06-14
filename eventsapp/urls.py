from django.urls import path
from .views import *
urlpatterns = [
    path('register/<int:userid>/<int:eventid>/',register_into_event),
    path('unregister/<int:userid>/<int:eventid>/',unregister_from_event),
    path('',homepageview)
]