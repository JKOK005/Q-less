from django.shortcuts import render
from django.views.generic import View, TemplateView
from UpdateSeats.models import *
from StoreDetails.models import FifoServiceQueue
from django.http import HttpResponse, JsonResponse

# Create your views here.
class GetWaitingTime(View):
	def get(self, request, *args, **kwargs):
		json_dict			= {"wait":30,}
		return JsonResponse(json_dict)	

class GetVacantSeats(View):
	def get(self, request, *args, **kwargs):
		json_dict 			= {"sid":-1,}
		seat_is_available 	= OccupancyModels.objects.filter(occupancy=False).first()
		if(seat_is_available):
			json_dict["sid"] 	= seat_is_available.pk

		return JsonResponse(json_dict)

class GetNoAvailableSeats(View):
	def get(self, request, *args, **kwargs):
		json_dict 			= {"seats_available":OccupancyModels.objects.filter(occupancy=False).count()}
		return JsonResponse(json_dict)	

class NotifySeatAvailable(View):
	def get(self, request, *args, **kwargs):
		json_dict 			= {"sid":-1, "wait":0}
		order_id 			= int(kwargs["order_id"])
		seat_is_available 	= OccupancyModels.objects.filter(occupancy=False).first()
		if(seat_is_available and FifoServiceQueue.objects.order_by('time_stamp').first().pk == order_id):
			json_dict["sid"] 	= seat_is_available.pk

		else:
			json_dict["wait"] 	= 30
		return JsonResponse(json_dict)

# Main page view
class GetMainView(TemplateView):	
	template_name 				= "index.html"
