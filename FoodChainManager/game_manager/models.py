from django.db import models

# Create your models here.
class GameSession(models.Model):
    session_id = models.IntegerField(primary_key=True, default=1, unique=True, null=False) # Force the session_id to be unique
    game_open = models.BooleanField(default=False) # Allow game to be seen
    
    def __str__(self):
        return "Session " + str(self.session_id)


class GameSessionPlayer(models.Model):
    session_id = models.ForeignKey(GameSession, on_delete=models.CASCADE, default=0) # If we delete the session, delete this as well
    player_id = models.IntegerField(unique=True, default=1) # Unique identifier for the player
    player_name = models.CharField(max_length=200) # Representable name for that player

    def __str__(self):
        return self.player_name

class GameSessionHistory(models.Model):
    session_id = models.ForeignKey(GameSession, on_delete=models.CASCADE, default=0) # If we delete the session, delete this as well
    turn_id = models.PositiveIntegerField(default=1) # What turn this event took on
    player_id = models.ForeignKey(GameSessionPlayer, on_delete=models.RESTRICT, default=None) # The player that performed this event
    
    def __str__(self):
        return "Turn: " + str(self.turn_id) + " by " + str(self.player_id)
