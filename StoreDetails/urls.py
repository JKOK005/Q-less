from django.conf.urls import url
from django.contrib import admin
from StoreDetails.views import *

# store-details
urlpatterns = [
	url(r'^check-order/(?P<store_id>[0-9])/$', GetStoreOrderQueue.as_view(), name="get-store-order-queue"),
]