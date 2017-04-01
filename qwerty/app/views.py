from django.http import HttpResponse
from models import Event
from django.shortcuts import render

def index(request):
    all_entries = Event.objects.all()
    print(all_entries)
    return render(request, './index.html', {'test': 'aaa'})
    return HttpResponse("Hello, world.")