from apiip import apiip
from pprint import pprint
from django.http import HttpResponse
from django.shortcuts import render


import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import time
# from playsound import playsound
# import openai
import pyjokes
import requests
from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv
load_dotenv()
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def home(request):
    if request.method == "POST":
        data = request.POST.get("speech","")
        print("this is data", data)
        if "hello" in data:
         return render(request, 'index.html', {'output':"hii"})
    return render(request, 'index.html')
