from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Event
		fields = ('id','title','date','location_lat','location_lng','marker_type',)

class EventDetailSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Event
		fields = ('id','description','created',)