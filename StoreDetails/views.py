from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, JsonResponse
from django.utils import timezone
from StoreDetails.models import *
import json

# Create your views here.
class GetStoreOrderQueue(View):
	def get(self, request, *args, **kwargs):
		try:
			json_dict 		= {"menu":[], "queue_no":[]}
			store 			= StoreModels.objects.filter(pk=kwargs['store_id']).first()
			food_menu_list 	= store.foodmenumodels_set.all()
			for each_food_menu in food_menu_list:
				each_food_in_queue 	= each_food_menu.fifoservicequeue_set.all()
				json_dict["menu"].append(each_food_menu.pk)
				json_dict["queue_no"].append(each_food_in_queue.count())

			return JsonResponse(json_dict)

		except Exception as e:
			return HttpResponse(e)

class NextOrderInQueue(View):
	def get(self, request, *args, **kwargs):
		json_dict 		= {"to_prep":-1}
		store 			= StoreModels.objects.filter(pk=kwargs['store_id']).first()
		to_prep 		= store.fifoservicequeue_set.order_by('time_stamp').first()
		if(to_prep):
			json_dict["to_prep"] 	= to_prep.food_menu.pk
		return JsonResponse(json_dict)

class RemoveStoreOrderQueue(View):
	def get(self, request, *args, **kwargs):
		store 			= StoreModels.objects.filter(pk=kwargs['store_id']).first()
		to_prep 		= store.fifoservicequeue_set.order_by('time_stamp').first()
		if(to_prep):
			to_prep.delete()
		return HttpResponse("Deletion done")

class AddNewOrdersToQueue(View):
	def get(self, request, *args, **kwargs):
		try:
			store 			= StoreModels.objects.filter(pk=kwargs['store_id']).first()
			food_menu 		= store.foodmenumodels_set.filter(pk=kwargs['food_menu_id']).first()
			time_now 		= timezone.now()
			FifoServiceQueue.objects.create(store_id=store, food_menu=food_menu, time_stamp=time_now)
			return HttpResponse("Added new item to queue")
		except Exception as e:
			return HttpResponse(e)