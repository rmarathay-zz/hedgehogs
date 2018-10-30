from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.postgres.fields import ArrayField
# Create your models here.

class Daily_Price_Info(models.Model):
	data = models.CharField(max_length=250)
	price = models.FloatField(default = False)
	date = models.DateTimeField(auto_now_add=True)
	open_data = models.FloatField(default = False)  
	high = models.FloatField(default = False)
	low = models.FloatField(default = False)
	close = models.FloatField(default = False)
	volume = models.FloatField(default = False)
	percent_change = models.FloatField(default = False)
	week_high_52 = models.FloatField(default = False)
	week_low_52 = models.FloatField(default = False)


	def __str__(self):
		return str(self.data)

	class Meta:
		app_label = 'analytics'
		verbose_name = "Daily_Price_Info"

class Company_Info(models.Model):
	company_id = models.FloatField(default = False)
	ticker = models.CharField(max_length=250)
	company_name = models.CharField(max_length=250)

	def __str__(self):
		return str(self.company_name)

	class Meta:
		app_label = 'analytics'
		verbose_name = "Company_Info"


class Time_Series(models.Model):
	ts_id = models.FloatField(default = False)
	company_id = models.FloatField(default = False)
	ticker = models.CharField(max_length=250)
	price = models.FloatField(default = False)
	date = models.DateTimeField(auto_now_add=True)
	open_data = models.FloatField(default = False)  
	high = models.FloatField(default = False)
	low = models.FloatField(default = False)
	close = models.FloatField(default = False)


	def __str__(self):
		return str(self.company_id)

	class Meta:
		app_label = 'analytics'
		verbose_name = "Time_Series"

class Fundamentals(models.Model):
	c_id = models.FloatField(default = False)
	company_name = company_name = models.CharField(max_length=250)
	common_shares_outstanding = models.FloatField(default = False)
	price = models.FloatField(default = False)
	date = models.DateTimeField(auto_now_add=True)
	open_data = models.FloatField(default = False)  
	high = models.FloatField(default = False)
	low = models.FloatField(default = False)
	close = models.FloatField(default = False)
	volume = models.FloatField(default = False)
	percent_change = models.FloatField(default = False)
	week_high_52 = models.FloatField(default = False)
	week_low_52 = models.FloatField(default = False)

	def __str__(self):
		return str(self.company_name)

	class Meta:
		app_label = 'analytics'
		verbose_name = "Fundamentals"