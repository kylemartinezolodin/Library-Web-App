from django.views.generic import View
from django.shortcuts import redirect, render
import re
import json
from datetime import datetime, timedelta

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

class BookView(View):
    def get(self,request):
        return render(request, 'index/UI-Books.html')

class BoothView(View):
    def get(self,request):
        return render(request, 'index/UI-Booths.html')


    #Merged
class MapIndexView(View):
    def get(self, request):
        return render(request, 'mapTemplates/map.html')

class alfred(View):
    def get(self, request):
        return render(request, 'alfred/index.html')

class SearchUIView(View):
    def get(self,request):
        b = Material.objects.first()
        # print(b)
        final = list()
        date = datetime.now().date()   
        dated = date - timedelta(days=30)
        
        
        c = Material_Borrow.objects.raw('''SELECT *,count(Borrow_material_id) as Borrow_counter FROM Material_Borrow where Borrow_borrow_date BETWEEN '%s/%s/%s' AND '%s/%s/%s' GROUP BY Borrow_material_id ORDER BY Borrow_counter DESC limit 3 ''',[dated.year,dated.month,dated.day,date.year,date.month,date.day])        
        print(c[0].Borrow_material.Material_title)
        context = {
            'mat': b,
            'trends':c
        }
        return render(request,'mat/searchUI.html', context)

def LiveSearch(request):
    filt = request.GET.getlist("d")[0]
    d=""
    mat = Material.objects.filter(Material_title__icontains=filt)
    #print(mat[0])
    for objects in mat:
        d += "<div class='result' id='outer' style='align-content:center;  padding: 15px 30px 15px 30px; margin: auto;'><div class='row' id='inner' style='border-radius: 4px; padding: 15px 10px 15px 5px;'><div class='col-2'><img src='/static/res/"+objects.Material_image+"' alt='' srcset='' width='140px' height='170px'></div><div class='col'><h3 style='color: white;'>"+objects.Material_title+"</h3> <!-- TTILE --><h6 style='color: white;'>"+objects.Material_author.lastname+", "+objects.Material_author.firstname+"</h6> <!-- Author --><p style='color: white; text-align: justify;'>"+objects.Material_preface+"</p> <!-- preface --></div></div></div>"
    #print(d)
    return JsonResponse({"d": d})
