from django.conf.urls import url
from django.contrib import admin
from UpdateSeats.views import *

# update
urlpatterns = [
	url(r'^seat-occupancy/$', UpdateSeatOccupancy.as_view(), name="seat-occupancy"),
]