from django.db import models
from datetime import datetime
from comstudreserve.models import Student
# Create your models here.
class Booth(models.Model):
	Booth_equipment = models.CharField(max_length = 100)
	Booth_cost = models.DecimalField(max_digits=5, decimal_places=2)

	class Meta:
		db_table = "Booth"

	def __str__(self):
		return self.Booth_equipment

class Timeslot(models.Model):
	Timeslot_start_time = models.TimeField(auto_now=False, auto_now_add=False)
	Timeslot_end_time = models.TimeField(auto_now=False, auto_now_add=False)

	class Meta:
		db_table = "Timeslot"

class Booth_Reserve(models.Model):
	BReserve_student = models.ForeignKey(Student, on_delete=models.CASCADE)
	BReserve_booth = models.ForeignKey(Booth, on_delete=models.CASCADE)
	BReserve_timeslot = models.ForeignKey(Timeslot, on_delete=models.CASCADE)
	CReserve_date = models.DateField()
	CReserve_date = models.TimeField(auto_now=False, auto_now_add=False)

	class Meta:
		db_table = "Booth_Reserve"
