from magazinesapp.models import MagazineModel
from django.shortcuts import render
from .models import MagazineModel
# Create your views here.
def homepageview(request):
    magazines = MagazineModel.objects.all()
    context = {
        'magazines' : magazines,
        'is_logged' : request.user.is_authenticated,
        'user' : request.user,
        }
    return render(request,"magazinesapp/index.html",context)