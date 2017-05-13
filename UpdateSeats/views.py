from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from UpdateSeats.models import  *
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json

# Create your views here.
class SeatAvailability(View):
	@method_decorator(csrf_exempt)
	def dispatch(self, *args, **kwargs):
		return super(SeatAvailability, self).dispatch(*args, **kwargs)

	def post(self, request, *args, **kwargs):
		try:
			json_rcv_obj	= json.loads(request.body.decode('utf-8'))
			no_of_seated 	= 0	
			ID 				= json_rcv_obj['sid']
			is_occupied 	= json_rcv_obj['occupancy']
			zipped			= zip(ID, is_occupied)
			
			for each_itr in zipped:
				each_id 			= each_itr[0]
				each_is_occupied 	= each_itr[1]
				
				if(each_is_occupied):
					no_of_seated 	+= 1
				seat 				= OccupancyModels.objects.filter(id=each_id).update(occupancy=each_is_occupied)

			time_now 	= timezone.now()
			obj 		= TableOccupancyTimeModels.objects.create(time_stamp=time_now, no_of_occupied_seats=no_of_seated)
			obj.save()

			return HttpResponse("Success in updating seat occupancy")
		except Exception as e:
			return HttpResponse("Failed to update seat occupancy")

	def get(self, request, *args, **kwargs):
		return HttpResponse("Querying seat")
