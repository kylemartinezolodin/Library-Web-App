from django.db import models
from datetime import datetime
# Create your models here.
class Administrator(models.Model):
	Administrator_username = models.CharField(max_length = 100)
	Administrator_firstname = models.CharField(max_length = 100)
	Administrator_lastname = models.CharField(max_length = 100)
	Administrator_password = models.CharField(max_length = 100)

	class Meta:
		db_table = "Administrator"



class Announcement(models.Model):
	Announcement_type = models.CharField(max_length = 100)
	Announcement_title = models.CharField(max_length = 100)
	Announcement_content = models.CharField(max_length = 100)
	Announcement_date = models.DateField()
	Announcement_author = models.ForeignKey(Administrator, on_delete=models.CASCADE)

	class Meta:
		db_table = "Announcement"