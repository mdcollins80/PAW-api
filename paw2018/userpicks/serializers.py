from .models import UserPick
from rest_framework import serializers
from paw2018.nflteams.serializers import TeamIDSerializer
from paw2018.nflgames.serializers import GameIDSerializer
from paw2018.userteams.serializers import UserTeamIDSerializer


class UserPickSerializer(serializers.ModelSerializer):
    team = UserTeamIDSerializer(read_only=True)
    game = GameIDSerializer(read_only=True)
    pick = TeamIDSerializer(read_only=True)

    class Meta:
        model = UserPick
        fields = ('id', 'team', 'game', 'pick', 'correct')


class UserPickPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPick
        fields = ('id', 'team', 'game', 'pick')
