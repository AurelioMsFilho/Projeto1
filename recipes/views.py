from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    return render (request, 'recipes/home.html', context={
        'nome': 'Aurélio Filho', 
    })

def sobre(request):
    return render (request,'arquivo.html')

def contato(request):
    return render (request, 'temp.html')

def biblioteca(request):
    return HttpResponse('biblioteca')

def audio_video(request):
    return render(request, 'audio.html')

