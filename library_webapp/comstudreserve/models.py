from django.db import models
from datetime import datetime
# Create your models here.
class Student(models.Model):
	Student_firstname = models.CharField(max_length = 100)
	Student_lastname = models.CharField(max_length = 100)

	class Meta:
		db_table = "Student"

class Computer(models.Model):
	Computer_number = models.CharField(max_length = 10)

	class Meta:
		db_table = "Computer"

class Computer_Reserve(models.Model):
	CReserve_student = models.ForeignKey(Student, on_delete=models.CASCADE)
	CReserve_computer = models.ForeignKey(Computer, on_delete=models.CASCADE)
	CReserve_date = models.DateField()
	CReserve_start_time = models.TimeField(auto_now = False, auto_now_add = False)
	CReserve_end_time = models.TimeField(auto_now = False, auto_now_add = False)

	class Meta:
		db_table = "Computer_Reserve"


class Reservation_Queue(models.Model):
	Queue_student = models.ForeignKey(Student, on_delete=models.CASCADE)
	Queue_datetime = models.DateField()

	class Meta:
		db_table = "Reservation_Queue"

