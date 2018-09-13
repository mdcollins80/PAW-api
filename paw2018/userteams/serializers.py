from .models import UserTeam
from rest_framework import serializers

class UserTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTeam
        fields = ('id', 'owner', 'league', 'team_name')
