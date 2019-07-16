from django.db import models

# Create your models here.
class Pet(models.Model):
	name = models.CharField(max_length=10)
	age = models.IntegerField()
	available = models.BooleanField()
	Image = models.ImageField()
	price = models.DecimalField(max_digits=10, decimal_places=3)

	def __str__(self):
		return self.name