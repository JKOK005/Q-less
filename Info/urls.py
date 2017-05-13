from django.conf.urls import url
from django.contrib import admin
from Info.views import *

# info
urlpatterns = [
	url(r'^waiting-time/$', GetWaitingTime.as_view(), name="waiting-time"),
	url(r'^vacant-seats/$', GetVacantSeats.as_view(), name="vacant-seats"),
]