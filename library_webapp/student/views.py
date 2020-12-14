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
        b = Material.objects.last()
        print(b)
        c = Material_Borrow.objects.all()
        cx = list()
        count = [3]
        i = 0
        for item in c:
            cx.append(item)
            print(item)
            print(cx[i].Borrow_material)
            i+=1
            print(item.Borrow_material_id)
            x=item.Borrow_material_id-1
            # count[x]+=1

        # count.sort(reverse=True)

        # for item in cx:
        #     if(count.index()==cx.Material_id):
        #         final.append(cx)


        context = {
            'mat': b
            # 'trends':final
        }
        return render(request,'mat/searchUI.html', context)

def LiveSearch(request):
    filt = request.GET.getlist("d")[0]
    d=""
    mat = Material.objects.filter(Material_title__icontains=filt)
    #print(mat[0])
    for objects in mat:
        d += "<div class='result' id='outer' style='align-content:center;  padding: 15px 30px 15px 30px; margin: auto;'><div class='row' id='inner' style='border-radius: 4px; padding: 15px 10px 15px 5px;'><div class='col-2'><img src='static/res/"+"' alt='' srcset='' width='140px' height='170px'></div><div class='col'><h3 style='color: white;'>"+objects.Material_title+"</h3> <!-- TTILE --><h6 style='color: white;'></h6> <!-- Author --><p style='color: white; text-align: justify;'>"+objects.Material_preface+"</p> <!-- preface --></div></div></div>"
    #print(d)
    return JsonResponse({"d": d})
