from django.shortcuts import render
from django.views.generic import View
# Create your views here.

class frameView(View):
    def get(self,request):
        return render(request, 'folder/frame.html')

#class studentIndexView(View):
    #def get(self,request):
        #return render(request, 'UI-Announcement.html')
