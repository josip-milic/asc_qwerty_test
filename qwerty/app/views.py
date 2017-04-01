from django.http import HttpResponse
from models import Event
from django.shortcuts import render
from django.core import serializers
from django.template import loader
from django.http import JsonResponse

def index(request):
    template = loader.get_template('app/index.html')
    return HttpResponse(template.render({}, request))
    
def get_events(request):
    events = Event.objects.all()
    data = serializers.serialize("json", [events])
    return data
    