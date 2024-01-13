from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    return render (request, 'home.html')

def sobre(request):
    return HttpResponse ('sobre')

def contato(request):
    return HttpResponse ('contato')

def biblioteca(request):
    return HttpResponse('biblioteca')

def audio_video(request):
    return render(request, 'audio.html')

