from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^ajax/get_events/$', views.get_events, name='get_events'),
    url(r'^ajax/get_event/(?P<pk>[0-9]+)/$', views.get_event, name='get_event'),
]