from .models import Game
from rest_framework import serializers

class GameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Game
        fields = ('__str__', 'week_num', 'weekday', 'kickoff', 'season',
                  'home_team', 'home_team_score', 'away_team', 'away_team_score')
