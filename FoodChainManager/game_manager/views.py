from django.shortcuts import render, HttpResponse, get_object_or_404

from .models import GameSession, GameSessionPlayer, GameSessionHistory

# Create your views here.
def index(request):
    sessions = GameSession.objects.filter(game_open=True)

    return render(request, 'game_manager/index.html', {'sessions': sessions})

def session(request, session_id):
    try:
        current_session = get_object_or_404(GameSession, pk=session_id)
    except (KeyError):
        return HttpResponse("This game session does not exist")
    else:
        return render(request, 'game_manager/session.html', {'session': current_session })