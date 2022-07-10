from django.db import models

# Create your models here.
class GameSession(models.Model):
  session_id = models.IntegerField(primary_key=True) # Force the session_id to be unique



class GameSessionPlayers(models.Model):
  session_id = models.ForeignKey(GameSession, on_delete=models.CASCADE) # If we delete the session, delete this as well
  


class GameSessionHistory(models.Model):
  session_id = models.ForeignKey(GameSession, on_delete=models.CASCADE) # If we delete the session, delete this as well

