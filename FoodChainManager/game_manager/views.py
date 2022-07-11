from django.shortcuts import render, HttpResponse

from .models import GameSession, GameSessionPlayer, GameSessionHistory

# Create your views here.
def index(request):
    sessions = GameSession.objects.filter(game_open=True)

    return render(request, 'game_manager/index.html', {'sessions': sessions})

    