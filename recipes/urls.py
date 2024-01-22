from django.urls import path
from recipes.views import contato, home, sobre, biblioteca, audio_video

urlpatterns = [
    path('', home ),
    path('sobre/', sobre ),
    path('contato/', contato),
    path('biblioteca/', biblioteca),
    path('audio_video/', audio_video ),
    
]

