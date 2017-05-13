from django.db import models

# Create your models here.
class OccupancyModels(models.Model):
	occupancy = models.BooleanField(default=False)

class TableOccupancyTimeModels(models.Model):
	time_stamp 				= models.DateTimeField(auto_now=False)
	no_of_occupied_seats 	= models.IntegerField(default=0)