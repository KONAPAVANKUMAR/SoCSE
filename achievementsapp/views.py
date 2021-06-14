from django.shortcuts import render,redirect
from .models import *
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
# Create your views here.
def addachievementview(request):
    if not request.user.is_authenticated:
        messages.add_message(request,messages.ERROR,'you are not logged in')
        return redirect("indexpageview")
    context = {
        'is_logged' : request.user.is_authenticated,
        'user' : request.user,
    }
    return render(request,"achievementsapp/addachievement.html",context)

import os
from django.conf import settings
def addachievement(request):
    
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        logo_url = os.path.join(settings.MEDIA_URL, 'achievements/')
        logoRoot = os.path.join(settings.MEDIA_ROOT, 'achievements/')
        
        fs = FileSystemStorage(location=logoRoot)
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = logo_url+filename
        print(uploaded_file_url)
        print(filename)
        AchievementModel(
            user = request.user,
            description = request.POST['description'],
            date = request.POST['date'],
            proof = f'achievements/{filename}'

        ).save()
    messages.add_message(request,messages.INFO,'your achievement was submitted for approval')
    return redirect("indexpageview")

def homepageview(request):
    achievements = AchievementModel.objects.all()
    context = {
        'achievements' :achievements,
        'is_logged' : request.user.is_authenticated,
        'user' : request.user,
    }
    return render(request,"achievementsapp/index.html",context)