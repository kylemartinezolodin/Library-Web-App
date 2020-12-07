
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView
from django.http import HttpResponse
from .models import Material,Material_Borrow,Author

# Create your views here.

class MatView(View):
    def get(self,request):
        return render(request,'mat.html')

class Mat1View(View):
    def get(self,request):
        q1 = Material.objects.get(Material_id=3)
        q2 = Material_Borrow.objects.all()
        q3 = Author.objects.all()
        context0 ={
            'mat' : q1
        }
        for matb in q2:
            context1 = {
                'matb' : q2
            }
        for author in q3:
            context2 = {
                'author' : q3
            }
        return render(request,'mat1.html',context0)