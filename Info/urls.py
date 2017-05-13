from django.conf.urls import url
from django.contrib import admin
from Info.views import *

# info
urlpatterns = [
	url(r'^waiting-time/$', GetWaitingTime.as_view(), name="waiting-time"),
	url(r'^vacant-seats/$', GetVacantSeats.as_view(), name="vacant-seats"),
	url(r'^no-of-available-seats/$', GetNoAvailableSeats.as_view(), name="no-available-seats"),
	url(r'^notify-seat-vacant/(?P<order_id>\d{1,3})/$', NotifySeatAvailable.as_view(), name="notify-seat-vacant"),
]