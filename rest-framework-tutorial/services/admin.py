from django.contrib import admin

from .models import Event

class EventAdmin(admin.ModelAdmin):
	list_display = ('title','date','location_lat','location_lng','marker_type','description')
	
admin.site.register(Event, EventAdmin)
