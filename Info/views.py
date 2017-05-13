from django.shortcuts import render
from django.views.generic import View
from UpdateSeats.models import *
from django.http import HttpResponse
import IPython

# Create your views here.
class GetWaitingTime(View):
	def get(self, request, *args, ** kwargs):
		pass

class GetVacantSeats(View):
	def get(self, request, *args, ** kwargs):
		vacant_seat 	= OccupancyModels.objects.filter(occupancy=False).first()
		if(vacant_seat):
			return HttpResponse("Vacant seat id: {0}".format(vacant_seat.pk))
		return HttpResponse("No vacant seats")