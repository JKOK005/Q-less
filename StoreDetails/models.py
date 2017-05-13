from django.db import models

# Create your models here.
class StoreModels(models.Model):
	store_name 		= models.CharField(max_length=50, default="Your store here")

	def __str__(self):
		return "Store name - {0}".format(self.store_name)

class FoodMenuModels(models.Model):
	store_id 		= models.ForeignKey(StoreModels, on_delete=models.CASCADE)
	food_name		= models.CharField(max_length=50)

	def __str__(self):
		return "Food menu - {0}".format(self.food_name)

class FoodOrderQueueModels(models.Model):
	food_menu 		= models.ForeignKey(FoodMenuModels, on_delete=models.CASCADE)
	queue_no 		= models.IntegerField(default=0)
	waiting_time 	= models.FloatField(default=9)

	def __str__(self):
		return "Food queue - {0}".format(self.food_menu.food_name)