from .models import Game
from rest_framework import serializers
from paw2018.nflteams.serializers import TeamNameSerializer

class GameSerializer(serializers.ModelSerializer):
    away_team = TeamNameSerializer(read_only=True)
    home_team = TeamNameSerializer(read_only=True)

    class Meta:
        model = Game
        fields = ('id', '__str__', 'week_num', 'weekday', 'kickoff', 'season',
                  'home_team', 'home_team_score', 'away_team', 'away_team_score',
                  'winner')
