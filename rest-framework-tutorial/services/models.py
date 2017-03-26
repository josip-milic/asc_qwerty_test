from django.db import models

class Event(models.Model):
	title = models.CharField(max_length=255)
	date = models.DateTimeField()
	description = models.TextField()

	def __unicode__(self):
		return self.title