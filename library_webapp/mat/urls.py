from django.urls import path
from . import views

app_name = 'mat'
urlpatterns = [
    path('',views.MatView.as_view(),name="mat_view"),
]