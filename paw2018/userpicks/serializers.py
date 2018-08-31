from .models import UserPick
from rest_framework import serializers

class UserPickSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserPick
        fields = ('team', 'game', 'pick')
