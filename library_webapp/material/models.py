from django.db import models
from datetime import datetime
from comstudreserve.models import Student


class Author(models.Model):
	firstname = models.CharField(max_length = 100)
	lastname = models.CharField(max_length = 100)	

	class Meta:
		db_table = "Author"

	def __str__(self):
		return self.lastname

class Material(models.Model):
	Material_type = models.CharField(max_length = 100)
	Material_title = models.CharField(max_length = 100)

	# Material_author = models.ForeignKey(Author, on_delete=models.CASCADE)
	# Material_publication = models.DateField()
	# Material_shelf_rack = models.CharField(max_length = 10)
	# Material_image = models.ImageField(blank = True)
	
	Material_author = models.ForeignKey(Author, blank=True,on_delete=models.CASCADE)
	Material_publication = models.DateField()
	Material_shelf_rack = models.CharField(max_length = 10)
	Material_image = models.CharField(max_length=30,blank=True)

	Material_preface = models.CharField(max_length = 300)

	class Meta:
		db_table = "Material"

	def __str__(self):
		return self.Material_title

class Material_Borrow(models.Model):
	Borrow_student = models.ForeignKey(Student, on_delete=models.CASCADE)
	Borrow_material = models.ForeignKey(Material, on_delete=models.CASCADE)
	Borrow_borrow_date = models.DateField()
	Borrow_return_date = models.DateField()
	Borrow_returned_date = models.DateField()

	class Meta:
		db_table = "Material_Borrow"

	def __str__(self):
		return self.Borrow_material
