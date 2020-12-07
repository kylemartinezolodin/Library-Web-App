from django.db import models
from datetime import datetime

# Create your models here.

class Material(models.Model):
    Material_id = models.IntegerField()
    Material_type = models.CharField(max_length=100)
    Material_title = models.CharField(max_length=100)
    Material_author = models.IntegerField()
    Material_publication_date = models.DateField()
    Material_shelf_rack = models.CharField(max_length=10)
    Material_image = models.CharField(max_length=100)
    Material_preface = models.CharField(max_length=300)
    
    class meta:
        db_table = "Material"

class Material_Borrow(models.Model):
    Borrow_id = models.IntegerField()
    Borrow_student = models.IntegerField()
    Borrow_material = models.IntegerField()
    Borrow_borrow_date = models.DateField()
    Borrow_return_date = models.DateField()
    Borrow_returned_date = models.DateField()

    class meta:
        db_table = "Material_Borrow"

class Author(models.Model):
    Author_id = models.IntegerField()
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)

    class meta:
        db_table = "Author"