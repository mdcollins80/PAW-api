from .models import Team
from rest_framework import serializers

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('id', 'location', 'name', 'conference', 'division',
                  'wins', 'losses', 'division_wins', 'division_losses')

class TeamNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('id', 'name')
