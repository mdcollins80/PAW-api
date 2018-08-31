from rest_framework import viewsets
from .serializers import TeamSerializer
from .models import Team

# Create your views here.
class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
