from django.http import HttpResponse
from models import Event

def index(request):
    all_entries = Event.objects.all()
    print('aaa')
    print(all_entries)
    return HttpResponse("Hello, world. You're at the polls index.")