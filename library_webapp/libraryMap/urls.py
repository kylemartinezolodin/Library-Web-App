from django.urls import path
from django.views.generic import TemplateView
from libraryMap import views
import libraryMap

# Create your views here.
app_name = 'libraryMap'
urlpatterns = [
    path('test', views.TestIndexView.as_view(), name="testView"),
    path('', views.MapIndexView.as_view(), name="mapView")
]
