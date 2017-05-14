from django.conf.urls import url
from django.contrib import admin
from StoreDetails.views import *

# store-details
urlpatterns = [
	url(r'^check-order/(?P<store_id>[0-9])/$', GetStoreOrderQueue.as_view(), name="get-store-order-queue"),
	url(r'^next-order/(?P<store_id>[0-9])/$', NextOrderInQueue.as_view(), name="next-order-in-queue"),
	url(r'^multi-queue-order/(?P<store_id>[0-9])/$', MultiOrdersInQueue.as_view(), name="multi-queue-order"),
	url(r'^remove-order/(?P<store_id>[0-9])/$', RemoveStoreOrderQueue.as_view(), name="remove-store-order"),
	url(r'^add-new-order/(?P<store_id>[0-9])/(?P<food_menu_id>[0-9])/$', AddNewOrdersToQueue.as_view(), name="add-new-order"),
]