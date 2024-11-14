from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def data(request):
    return HttpResponse("<h1>Это страница Data</h1><p>Содержимое страницы Data.</p>")

def test(request):
    return HttpResponse("<h1>Это страница Test</h1><p>Содержимое страницы Test.</p>")