from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

import datetime

# Create your views here.
def index(request):
    return HttpResponse("Bienvenue sur l'application Sondages !")

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

class CurrentDatetimeView(View):
    def get(self, request, *args, **kwargs):
        now = datetime.datetime.now()
        html = "<html><body>It is now %s.</body></html>" % now
        return HttpResponse(html)
    
class ArchiveView(View):
    def get(self, request, year, month):
        print(year)  # 2014
        print(month)  # 12
        html = "<html><body>It {} is now {}.</body></html>".format(year, month)
        return HttpResponse(html)