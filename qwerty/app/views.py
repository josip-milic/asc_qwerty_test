from django.http import HttpResponse
from .models import Event
from django.shortcuts import render
from django.core import serializers
from django.template import loader
from django.http import JsonResponse

def index(request):
    template = loader.get_template('app/index.html')
    return HttpResponse(template.render({}, request))
    
def get_events(request):
    events = Event.objects.all()
    data = serializers.serialize("json", events)
    return JsonResponse(data, safe = False)
    
def get_event(request,pk):
    events = Event.objects.filter(pk=pk)
    data = serializers.serialize("json", events)
    return JsonResponse(data, safe = False)
    
def post_event(request):
    data = request.POST
    title = data['title']
    date = data['date']
    location_lat = data['location_lat']
    location_lng = data['location_lng']
    marker_type = data['markerType']
    description = data['description']
    
    event = Event(title=title,date = date, location_lat=location_lat, location_lng=location_lng,description=description, marker_type = marker_type)
    event.save()
    return JsonResponse(str(event.id), safe = False)
    