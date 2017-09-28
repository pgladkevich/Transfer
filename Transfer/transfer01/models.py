from django.db import models


# Create your models here.

class Transfer(models.Model):

	def __str__(self):
		return self.name

	source_slot = models.CharField(max_length=255)
	source_well = models.CharField(max_length=255)
	volume = models.FloatField()
	destination_slot = models.CharField(max_length=255)
	destination_well = models.CharField(max_length=255)