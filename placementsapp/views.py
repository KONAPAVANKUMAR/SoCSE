from django.shortcuts import render
from .models import *
# Create your views here.
def homepageview(request):
    placements = PlacementsModel.objects.all()
    placement_years = set()
    is_logged = request.user.is_authenticated
    for placement in placements:
        placement_years.add(str(placement.date.year))
    from collections import defaultdict
    total_companies = defaultdict(int)
    total_students = defaultdict(int)
    for year in placement_years:
        for placement in placements:
            if str(placement.date.year)==str(year):
                total_students[year] += len(placement.students)

    for year in placement_years:
        for placement in placements:
            if str(placement.date.year)==str(year):
                total_companies[year] += 1
    

    context = {
        'placement_years' : sorted(list(placement_years),reverse=True),
        'is_logged' : is_logged,
        'placements':placements,
        'user' : request.user,
        'total_companies' : total_companies.items(),
        'total_students' : total_students.items(),

    }
    return render(request,"placementsapp/index.html",context)