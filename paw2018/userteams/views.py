from rest_framework import viewsets
from .serializers import UserTeamSerializer
from .models import UserTeam

# Create your views here.
class UserTeamViewSet(viewsets.ModelViewSet):
    queryset = UserTeam.objects.all()
    serializer_class = UserTeamSerializer


class UserTeamOwned(viewsets.ModelViewSet):
    serializer_class = UserTeamSerializer

    def get_queryset(self):
        owner = self.request.user
        queryset = UserTeam.objects.filter(owner=owner)
        return queryset
