from .models import League
from rest_framework import serializers

class LeagueSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = League
        fields = ('owner', 'league_name')
