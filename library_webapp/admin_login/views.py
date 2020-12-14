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

class IndexView(View):
    def get(self,request):
        return render(request, 'admin_login/index.html')