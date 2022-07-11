from django.contrib import admin

from .models import GameSession, GameSessionPlayer, GameSessionHistory

# Register your models here.

class PlayersInline(admin.StackedInline):
    model = GameSessionPlayer
    extra = 0
class SessionInline(admin.StackedInline):
    model = GameSessionHistory
class SessionAdmin(admin.ModelAdmin):

    inlines = [PlayersInline, SessionInline]

admin.site.register(GameSession, SessionAdmin)