import json
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
from django.shortcuts import render
from mat.models import Material
from datetime import datetime

def LiveSearch(request):
    template_name = "index.html"
    filt = request.GET.getlist("d")[0]
    d=""
    mat = Material.objects.filter(title__icontains=filt)
    print(filt)
    for objects in mat:
        d += "<div class='result' id='outer' style='align-content:center;  padding: 15px 30px 15px 30px; margin: auto;'><div class='row' id='inner' style='border-radius: 4px; padding: 15px 10px 15px 5px;'><div class='col-2'><img src='{% static `res/"+object.image+"` %}' alt='' srcset='' width='140px' height='170px'></div><div class='col'><h3 style='color: white;'>"+objects.title+"</h3> <!-- TTILE --><h6 style='color: white;'></h6> <!-- Author --><p style='color: white; text-align: justify;'>"+objects.preface+"</p> <!-- preface --></div></div></div>"
    print(d)
    return JsonResponse({"d": d})
    #def get(self, request):
     #   if 'term' in request.GET:        
      #      qs = Material.objects.filter(title__icontains=request.GET.get('term'))
       #     titles = list()
        #    for material in qs:
         #       print(material)
          #      titles.append(material.title)
           # return JsonResponse(titles, safe=False)
            
        #return render(request, 'search.html')

class SearchView(View):
    def get(self, request):
        return render(request, 'search.html')

class MatView(View):
    def get(self,request):
        return render(request,'mat.html')

class Mat1View(View):
    def get(self,request):
        # q1 = Material.objects.get(Material_id=3)
        # q2 = Material_Borrow.objects.all()
        # q3 = Author.objects.all()
        # context0 ={
        #     'mat' : q1
        # }
        # for matb in q2:
        #     context1 = {
        #         'matb' : q2
        #     }
        # for author in q3:
        #     context2 = {
        #         'author' : q3
        #     }
        # return render(request,'mat1.html',context0)
        return render(request,'mat1.html')
# Create your views here.

class SearchUIView(View):
    def get(self,request):
        return render(request,'searchUI.html')