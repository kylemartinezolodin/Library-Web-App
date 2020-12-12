from django.views.generic import View
from django.shortcuts import redirect, render
import re
import json

from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.http import JsonResponse
from material.models import *
# Create your views here.

class StudentIndexView(View):
    def get(self,request):
        return render(request, 'index/UI-Announcement.html')

class MapView(View):
    def get(self,request):
        return render(request, 'index/UI-Map.html')

class AlfredView(View):
    def get(self,request):
        return render(request, 'index/UI-Alfred.html')

#def StudentIndexView(request):
    #return render(request, 'index/UI-Announcement.html')

#def MapView(request):
    #return render(request, 'index/UI-Map.html')
#Alfred
class alfred(View):
    def get(self, request):
        return render(request, 'alfred/index.html')

def alfredprocess(request):
    msgText = request.GET.getlist('msgText')[0]

    keywords={
        'greet': ['.*\\bhullo\\b.*', '.*\\bhow do you do\\b.*', '.*\\bhowdy\\b.*', '.*\\bhi\\b.*', '.*\\bhello\\b.*'],
        'apa': ['.*\\bapa\\b.*','.*\\bapa format\\b.*',],
        'mla': ['.*\\bmla\\b.*','.*\\bmla format\\b.*'],
        'time': ['.*\\btime\\b.*','.*\\bopen\\b.*','.*\\bclose\\b.*','.*\\bclosing\\b.*'],
        'search': ['^search\s".*"\s*'],
        'book': ['.*\\bbook of\\b.*','.*\\bbooks of\\b.*']
    }

    responses={
        'greet':'Hello! How can I help you?',
        'apa':'Surname, initial(s). (Date Published). Title of source. Location of publisher: publisher. Retrieved from URL',
        'mla':'Author name(s). \"Article Time\". Title of container, contributors, version, numbers, date of publication, location, Title of database, DOI or URL',
        'time':'We\'re Open only open on Weekdays from 00:00 till 00:00',
        'fallback':'I dont quite understand. Could you repeat that?',
        'search': '',
        'book': ''
    }

    keywords_dict={}
    for intent, keys in keywords.items():
        keywords_dict[intent]=re.compile('|'.join(keys))

    msgText = msgText.lower()
    matched_intent = None

    for intent,pattern in keywords_dict.items():
        if re.search(pattern, msgText):
            matched_intent=intent

    key='fallback'
    if matched_intent in responses:
        key = matched_intent
        if key == 'search':
            query = (re.findall(r'"([^"]*)"', msgText))[0].lower()

        elif key == 'book':
            query = (re.findall(r'of\s*([^"]*)', msgText))[0].lower()

        queries = Material.objects.filter(Material_title__icontains=query)
        print(type(queries))
        if queries.count() > 0:
            for ob in queries:
                responses[key] += "<b>[</b>" + ob.Material_title + "<b>]</b><br/>"
        else:
            key = 'fallback'


    r = responses[key]

    return JsonResponse({'r': r})
