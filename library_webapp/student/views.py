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
