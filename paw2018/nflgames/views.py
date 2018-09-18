from rest_framework import viewsets
from .serializers import GameSerializer
from .models import Game

# Create your views here.
class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all().order_by('id').prefetch_related('home_team', 'away_team')
    serializer_class = GameSerializer
