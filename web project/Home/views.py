from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound
from django.template.loader import render_to_string
# Create your views here.

def index(request):
    text=render_to_string("Home/index.html")
    return HttpResponse(text)

def login(request):
    text=render_to_string("Home/login.html")
    return HttpResponse(text)

def pageone(request):
    text=render_to_string("Home/page1.html")
    return HttpResponse(text)

def pagetwo(request):
    text=render_to_string("Home/page2.html")
    return HttpResponse(text)

def pagethree(request):
    text=render_to_string("Home/page3.html")
    return HttpResponse(text)

def pagefour(request):
    text=render_to_string("Home/page4.html")
    return HttpResponse(text)

def reg(request):
    text=render_to_string("Home/regester.html")
    return HttpResponse(text)




