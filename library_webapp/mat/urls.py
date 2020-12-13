from django.urls import path
from . import views
import mat


urlpatterns = [
    path('', views.SearchView.as_view(), name='SearchView'),
    path('template', views.SearchUIView.as_view(), name='SearchUIView'),
    path('v1',views.MatView.as_view(),name="mat_view"),
    path('v2',views.Mat1View.as_view(),name="mat1_view"),
    path('get/ajax/friend', views.LiveSearch, name = "LiveSearch"),
]