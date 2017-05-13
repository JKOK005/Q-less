from django.conf.urls import url
from django.contrib import admin
from UpdateSeats.views import *

# update
urlpatterns = [
	url(r'^seat-occupancy/$', SeatAvailability.as_view(), name="seat-availability"),
]