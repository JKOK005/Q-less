from django.contrib import admin
from StoreDetails.models import *

# Register your models here.
@admin.register(StoreModels)
class StoreModelsAdmin(admin.ModelAdmin):
	pass

@admin.register(FoodMenuModels)
class FoodMenuModelsAdmin(admin.ModelAdmin):
	pass

@admin.register(FoodOrderQueueModels)
class FoodOrderQueueModelsAdmin(admin.ModelAdmin):
	pass

