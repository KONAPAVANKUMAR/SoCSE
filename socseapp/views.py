from magazinesapp.models import MagazineModel
from django.shortcuts import render,redirect
from django.contrib.auth import logout

from announcementsapp.models import *
from magazinesapp.models import *


from django.contrib import messages
# Create your views here.
def indexview(request):
    if request.user.is_authenticated:
        if request.user.email.find("@kletech.ac.in")==-1:
            messages.add_message(request,messages.ERROR,"only university students are allowed")
            logout(request)
            return redirect('indexpageview')
    # print(request.user.get_full_name())
    
    
    announcements = AnnouncementsModel.objects.all()

    is_logged = request.user.is_authenticated

    
    
    # print(placement_years)

    context = {

        
        
        'is_logged' : is_logged,
        'user' : request.user,
        
        'announcements' :announcements,
        

        
        }
    


    return render(request,"socseapp/index.html",context)

def logoutuser(request):
    logout(request)
    return redirect("account_logout")