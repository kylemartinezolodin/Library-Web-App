from django.db import models
from datetime import datetime
# Create your models here.
class Administrator(models.Model):
	username = models.CharField(max_length = 100)
	firstname = models.CharField(max_length = 100)
	lastname = models.CharField(max_length = 100)
	password = models.CharField(max_length = 100)

	class Meta:
		db_table = "Administrator"

class Announcement(models.Model):
	type = models.CharField(max_length = 100)
	title = models.CharField(max_length = 100)
	content = models.CharField(max_length = 100)
	date = models.DateField()
	author = models.IntegerField()

	class Meta:
		db_table = "Announcement"