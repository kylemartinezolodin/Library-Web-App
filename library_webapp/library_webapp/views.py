from django.views import View
from django.shortcuts import redirect, render
from nltk.corpus import wordnet
import re
import json

from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.http import JsonResponse

class alfred(View):
    def get(self, request):
        return render(request, 'alfred/index.html')

def alfredprocess(request):
    msgText = request.GET.getlist('msgText')[0]
    
    list_syn={
        'hello': {'how do you do', 'howdy', 'hullo', 'hello', 'hi'},
        'apa': {'apa','APA','APA format', 'apa format'}
    }

    keywords={
        'greet': ['.*\\bhullo\\b.*', '.*\\bhow do you do\\b.*', '.*\\bhowdy\\b.*', '.*\\bhi\\b.*', '.*\\bhello\\b.*'],
        'apa': ['.*\\bapa\\b.*','.*\\bapa format\\b.*',],
        'mla': ['.*\\bmla\\b.*','.*\\bmla format\\b.*'],
        'time': ['.*\\btime\\b.*','.*\\bopen\\b.*','.*\\bclose\\b.*','.*\\bclosing\\b.*']
    }

    keywords_dict={}
    for intent, keys in keywords.items():
        keywords_dict[intent]=re.compile('|'.join(keys))

    responses={
    'greet':'Hello! How can I help you?',
    'apa':'Surname, initial(s). (Date Published). Title of source. Location of publisher: publisher. Retrieved from URL',
    'mla':'Author name(s). \"Article Time\". Title of container, contributors, version, numbers, date of publication, location, Title of database, DOI or URL',
    'time':'We\'re Open only open on Weekdays from 00:00 till 00:00',
    'fallback':'I dont quite understand. Could you repeat that?'
    }

    msgText = msgText.lower()
    matched_intent = None 

    for intent,pattern in keywords_dict.items():
        if re.search(pattern, msgText): 
            matched_intent=intent  

    key='fallback' 
    if matched_intent in responses:
        key = matched_intent 

    r = responses[key]

    return JsonResponse({'r': r})