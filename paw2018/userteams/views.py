from rest_framework import viewsets
from .serializers import UserTeamSerializer
from .models import UserTeam

# Create your views here.
class UserTeamViewSet(viewsets.ModelViewSet):
    queryset = UserTeam.objects.all()
    serializer_class = UserTeamSerializer
