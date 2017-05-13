from django.contrib import admin
from UpdateSeats.models import *

# Register your models here.
@admin.register(OccupancyModels)
class OccupancyModelsAdmin(admin.ModelAdmin):
	pass

# Register your models here.
@admin.register(TableOccupancyTimeModels)
class TableOccupancyTimeModelsAdmin(admin.ModelAdmin):
	pass
