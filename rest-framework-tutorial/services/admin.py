from django.contrib import admin

from .models import Message

class EventAdmin(admin.ModelAdmin):
	list_display = ('title','date', 'description')
	admin.site.register(Event, EventAdmin)
