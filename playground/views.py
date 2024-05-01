from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def ping(request):
    return HttpResponse('Pong!')


def index(request):
    return render(request, 'index.html')

def date(request):
    ahora = datetime.now().strftime('%b %dth, %Y -%H:%M hrs')
    return HttpResponse(f"Hi, this is a greeting from Django, at {ahora}")
    
