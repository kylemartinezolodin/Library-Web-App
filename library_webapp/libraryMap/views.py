from django.shortcuts import render
from django.views.generic import View

# Create your views here.

class MapIndexView(View):
    def get(self, request):
        return render(request, 'mapTemplates/map.html')

        
class TestIndexView(View):
    def get(self, request):
        return render(request, 'mapTemplates/index.html')
