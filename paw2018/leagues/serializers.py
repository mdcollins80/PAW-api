from .models import League
from rest_framework import serializers

class LeagueSerializer(serializers.ModelSerializer):
    class Meta:
        model = League
        fields = ('id', 'owner', 'league_name')
