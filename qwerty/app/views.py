from django.http import HttpResponse
from models import Event
from django.shortcuts import render
from .serializer import EventSerializer
from django.template import loader

def index(request):
    template = loader.get_template('app/index.html')
    return HttpResponse(template.render({}, request))
    
def get_events(request):
    events = Event.objects.all()
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data)
    