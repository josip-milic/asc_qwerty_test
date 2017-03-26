from django.shortcuts import render
from .models import Event
from rest_framework import viewsets
from .serializer import EventSerializer

class EventViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Event.objects.all()
	serializer_class = EventSerializer
