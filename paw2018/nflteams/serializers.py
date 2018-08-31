from .models import Team
from rest_framework import serializers

class TeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Team
        fields = ('location', 'name', 'conference', 'division',
                  'wins', 'losses', 'division_wins', 'division_losses')
