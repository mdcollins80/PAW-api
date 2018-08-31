from .models import UserTeam
from rest_framework import serializers

class UserTeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserTeam
        fields = ('owner', 'league', 'team_name')
