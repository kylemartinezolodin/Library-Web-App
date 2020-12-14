from django.contrib import admin
from .models import Author, Material, Material_Borrow
from comstudreserve.models import Student

# Register your models here.
admin.site.register(Author)
admin.site.register(Material)
admin.site.register(Material_Borrow)
admin.site.register(Student)