from rest_framework import viewsets
from .serializers import GameSerializer
from .models import Game

# Create your views here.
class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
