from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    output = myfun(request)
    return render(request,'index.html',{'output':output})

def myfun(request):
    return "Hello"