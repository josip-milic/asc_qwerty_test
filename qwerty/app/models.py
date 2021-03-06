from django.db import models

# Create your models here.
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
        return u'%s' % self.title
        
    def __str__(self):
        return ("{} | {} | {}...".format(self.title, self.date, self.description[:20])).encode('ascii', errors='replace')