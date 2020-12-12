from django.db import models
from datetime import datetime
# Create your models here.
class Booth(models.Model):
	Booth_equipment = models.CharField(max_length = 100)
	Booth_cost = models.DecimalField(max_digits=5, decimal_places=2)

	class Meta:
		db_table = "Booth"

class Booth_Reserve(models.Model):
	BReserve_student = models.IntegerField()
	BReserve_booth = models.IntegerField()
	BReserve_timeslot = models.TimeField(auto_now=False, auto_now_add=False)
	CReserve_date = models.DateField()
	CReserve_date = models.TimeField(auto_now=False, auto_now_add=False)

	class Meta:
		db_table = "Booth_Reserve"

class Timeslot(models.Model):
	Timeslot_start_time = models.TimeField(auto_now=False, auto_now_add=False)
	Timeslot_end_time = models.TimeField(auto_now=False, auto_now_add=False)

	class Meta:
		db_table = "Timeslot"