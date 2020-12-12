from django.db import models
from datetime import datetime
# Create your models here.

class Computer_Reserve(models.Model):
	CReserve_student = models.IntegerField()
	CReserve_computer = models.IntegerField()
	CReserve_date = models.DateField()
	CReserve_start_time = models.TimeField(auto_now = False, auto_now_add = False)
	CReserve_end_time = models.TimeField(auto_now = False, auto_now_add = False)

	class Meta:
		db_table = "Computer_Reserve"

class Computer(models.Model):
	Computer_number = models.CharField(max_length = 10)

	class Meta:
		db_table = "Computer"

class Reservation_Queue(models.Model):
	Queue_student = models.IntegerField()
	Queue_datetime = models.DateField()

	class Meta:
		db_table = "Reservation_Queue"

class Student(models.Model):
	Student_firstname = models.CharField(max_length = 100)
	Student_lastname = models.CharField(max_length = 100)

	class Meta:
		db_table = "Student"