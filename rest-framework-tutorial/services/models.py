from django.db import models

class Event(models.Model):
	title = models.CharField(max_length=255)
	date = models.DateTimeField()
	description = models.TextField()
	location_lat = models.DecimalField(max_digits=9, decimal_places=6)
	location_lng = models.DecimalField(max_digits=9, decimal_places=6)
	marker_type = models.CharField(max_length=255)
	created = models.DateTimeField(auto_now_add=True)
	

	def __unicode__(self):
		return self.title