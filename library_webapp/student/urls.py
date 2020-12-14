from django.urls import path
#from view.generic import views
from django.views.generic import TemplateView
from . import views
#import student

app_name = 'student'

urlpatterns = [
    path('', views.StudentIndexView.as_view(), name="StudentIndexView"),
    path('map/', views.MapView.as_view(),name="MapView"),
    path('alfred/', views.AlfredView.as_view(),name="AlfredView"),
    path('book/', views.BookView.as_view(),name="BookView"),
    path('booth/', views.BoothView.as_view(),name="BoothView"),

#Merged
    path('map/map/',views.MapIndexView.as_view(),name="map"),
    path('alfred/alfred/',views.alfred.as_view(),name="alfred"),
    path('book/book/',views.SearchUIView.as_view(),name="book"),

]
