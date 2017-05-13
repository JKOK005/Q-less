from django.conf.urls import url
from django.contrib import admin
from Info.views import *

# info
urlpatterns = [
	url(r'^get-waiting-time/$', GetWaitingTime.as_view(), name="get-waiting-time"),
	url(r'^get-vacant-seats/$', GetVacantSeats.as_view(), name="get-vacant-seats"),
]