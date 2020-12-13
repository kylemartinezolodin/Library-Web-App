from django.contrib import admin
from django.apps import apps

material = apps.get_app_config('mat')

for material, model in material.models.items():
    admin.site.register(model)
# Register your models here.