from django.urls import path
#from view.generic import views
from django.views.generic import TemplateView
from . import views
#import student

app_name = 'student'

urlpatterns = [
    path('', views.StudentIndexView.as_view(), name="StudentIndexView"),
    path('map', views.MapView.as_view(),name="MapView"),
    path('alfred', views.AlfredView.as_view(),name="AlfredView"),
    path('student/ajax/alfred', views.alfredprocess, name='alfredprocess'),
]
