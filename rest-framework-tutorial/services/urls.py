from django.conf.urls import url
from services import views

urlpatterns = [
    url(r'^events/$', views.EventList),
    url(r'^events/(?P<pk>[0-9]+)/$', views.EventDetail),
]