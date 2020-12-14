from django.urls import path, include
from user_booth import views

app_name = 'user_booth'

urlpatterns = [
    path('', views.UserBoothIndexView.as_view(), name="UserBoothIndexView"),
]

