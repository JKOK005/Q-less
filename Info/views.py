from django.shortcuts import render
from django.views.generic import View
from UpdateSeats.models import *
from django.http import HttpResponse, JsonResponse

# Create your views here.
class GetWaitingTime(View):
	def get(self, request, *args, ** kwargs):
		pass

class GetVacantSeats(View):
	def get(self, request, *args, ** kwargs):
		json_dict 			= {"sid":-1,}
		seat_is_available 	= OccupancyModels.objects.filter(occupancy=False).first()
		if(seat_is_available):
			json_dict["sid"] 	= seat_is_available.pk

		return JsonResponse(json_dict)