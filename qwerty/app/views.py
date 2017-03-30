from django.http import HttpResponse
from models import Event

def index(request):
    all_entries = Event.objects.all()
    print('aa')
    print(all_entries)
    g = open('test.txt','w+')
    g.write('aaa')
    g.write(all_entries[0].id)
    return HttpResponse("Hello, world. You're at the polls index.")