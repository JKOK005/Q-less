from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, JsonResponse
from StoreDetails.models import *
import json
import IPython

# Create your views here.
class GetStoreOrderQueue(View):
	def get(self, request, *args, **kwargs):
		try:
			json_dict 		= {"menu":[], "queue_no":[],}
			store 			= StoreModels.objects.filter(pk=kwargs['store_id']).first()
			food_menu_list 	= store.foodmenumodels_set.all()
			for each_food_menu in food_menu_list:
				food_queue_handle 	= each_food_menu.foodorderqueuemodels_set.first()
				json_dict["menu"].append(each_food_menu.pk)
				json_dict["queue_no"].append(food_queue_handle.queue_no)
			return JsonResponse(json_dict)

		except Exception as e:
			return HttpResponse(e)