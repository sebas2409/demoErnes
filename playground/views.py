from django.shortcuts import render
from django.http import HttpResponse


def ping(request):
    return HttpResponse('Pong!')


def index(request):
    return render(request, 'index.html')
