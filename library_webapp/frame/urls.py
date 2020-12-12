from django.urls import path
#from view.generic import views
from django.views.generic import TemplateView
from frame import views
import frame
import student
app_name = 'frame'

urlpatterns = [
    path('',  views.frameView.as_view(), name="frame_view"),
    #path('UI-Announcement.html', TemplateView.as_view(template_name="UI-Announcement.html")),
    #path('student', TemplateView.as_view(template_name="index/UI-Announcement.html"),
                 # name='student_view'),
]
