from django.shortcuts import render
from django.views.generic import View
from comstudreserve.models import * 
from booth.models import * 
from datetime import datetime, timedelta

# Create your views here.
class UserBoothIndexView(View):
    def get(self,request):
        qs_computer = Computer.objects.all()
        # qs_creserve = Computer_Reserve.objects.all()
        # __gt MEANS GREATER THAN

        # QUERY FOR RESERVATIONS THAT IS GREATER THAN datetime.now().time()
        qs_creserve = Computer_Reserve.objects.filter( CReserve_date = datetime.now().date(), CReserve_end_time__gt = datetime.now().time())
        
        

        available_computer_count = len(qs_computer)
        for not_available in qs_creserve:
            available_computer_count -= 1

        # print(qs_creserve[0].id)
        qs_booth = Booth.objects.all()

        # QUERY FOR RESERVATIONS THAT HAS NOT LOGGED THE CReserve_end_time (WHICH POSSIBLY MEANS THEY ARE STILL USING) 
        qs_breserve = Booth_Reserve.objects.filter( BReserve_date = datetime.now().date(), BReserve_end_time = None) 

        available_booth_count = len(qs_booth)
        for not_available in qs_breserve:
            available_booth_count -= 1

        context = {
            'booth_list' : qs_booth,
            'booth_count' : available_booth_count,
            'breserve_list' : qs_breserve,

            'computer_list' : qs_computer,
            'computer_count' : available_computer_count,
            'creserve_list' : qs_creserve,
        }

        return render(request, 'user_booth/index.html', context )
