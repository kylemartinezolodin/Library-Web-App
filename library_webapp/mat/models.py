from django.db import models
from datetime import datetime

class Material(models.Model):
	type = models.CharField(max_length = 100)
	title = models.CharField(max_length = 100)
	author = models.IntegerField()
	publication = models.DateField()
	shelf_rack = models.CharField(max_length = 10)
	image = models.ImageField()
	preface = models.CharField(max_length = 300)

	class Meta:
		db_table = "material"

class Author(models.Model):
	firstname = models.CharField(max_length = 100)
	lastname = models.CharField(max_length = 100)	

	class Meta:
		db_table = "Author"


#class Material_Borrow(models.Model):
#	student = models.IntegerField()
#	material = models.IntegerField()
#	borrow_date = models.DateField()
#	return_date = models.DateField()
#	returned_date = models.DateField()

#	class Meta:
#		db_borrow = "Material_Borrow"
