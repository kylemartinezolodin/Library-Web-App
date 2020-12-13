"""library_webapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import path, include

# ALFRED IMPPORT BLOCK
from . import views
from django.http import JsonResponse


urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/',include('student.urls', namespace='student')),
    #path('',include('student.urls')),
    path('frame/',include('frame.urls', namespace='iframe')),
    path('admin/', admin.site.urls),
    path('map/', include('libraryMap.urls', namespace='libraryMap')),
]

# MAP urlpatterns
urlpatterns += [
    path('admin/', admin.site.urls),
    path('map/', include('libraryMap.urls', namespace='libraryMap')),
]

# ALFRED urlpatterns
urlpatterns += [
    path('admin/', admin.site.urls),
    path('alfred',  views.alfred.as_view(), name='alfred'),
    path('ajax/alfred', views.alfredprocess, name='alfredprocess'),

# MATERIAL urlpatterns
urlpatterns += [
    path('admin/', admin.site.urls),
    path('',include('mat.urls')),
]
