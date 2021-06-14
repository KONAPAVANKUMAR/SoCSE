from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def register_into_event(request,userid,eventid):
    user = User.objects.get(id = userid)
    event = EventModel.objects.get(id = eventid)
    event.participants.append(user.email)
    event.save()
    messages.add_message(request,messages.SUCCESS,f"succesfully registered to {event.name}")
    return redirect(request.META['HTTP_REFERER'])

def unregister_from_event(request,userid,eventid):
    user = User.objects.get(id = userid)
    event = EventModel.objects.get(id = eventid)
    event.participants.remove(user.email)
    event.save()
    messages.add_message(request,messages.ERROR,f"unregistered from {event.name}")
    return redirect(request.META['HTTP_REFERER'])

def homepageview(request):
    events = sorted(EventModel.objects.all(),key=lambda t: (t.type.name,t.datetime))
    eventtypes = EventTypeModel.objects.all()
    is_logged = request.user.is_authenticated
    events_years = set()
    for event in events:
        events_years.add(str(event.datetime.date().year))
    context = {
        'eventtypes' : eventtypes,
        'events_years' : sorted(list(events_years),reverse=True),
        'is_logged' : is_logged,
        'user' : request.user,
        'events' : events,
        }
    return render(request,"eventsapp/index.html",context)