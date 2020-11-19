<<<<<<< HEAD
from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView
from django.http import HttpResponse

# Create your views here.

class MatView(View):
    def get(self,request):
        return render(request,'mat.html')
=======
from django.shortcuts import render

# Create your views here.
>>>>>>> 6e67ab2... added app called "mat"
