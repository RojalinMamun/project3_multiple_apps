from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def app1_first(request):
    return HttpResponse('<h1>This is the first views function of app1</h1>')

def app1_second(request):
    return HttpResponse('<h1> And this is the second view function of app1</h1>')