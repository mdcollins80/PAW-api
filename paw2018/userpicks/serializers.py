from .models import UserPick
from rest_framework import serializers

class UserPickSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPick
        fields = ('id', 'team', 'game', 'pick')
