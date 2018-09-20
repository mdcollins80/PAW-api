from rest_framework import viewsets
from .serializers import UserPickSerializer, UserPickPostSerializer
from .models import UserPick
from paw2018.userteams.models import UserTeam

# Create your views here.
class UserPickViewSet(viewsets.ModelViewSet):
    queryset = UserPick.objects.all().prefetch_related('pick','game','team')
    serializer_class = UserPickSerializer


class UserPickPostSet(viewsets.ModelViewSet):
    queryset = UserPick.objects.all().prefetch_related('pick','game','team')
    serializer_class = UserPickPostSerializer


class UserPickOwned(viewsets.ModelViewSet):
    serializer_class = UserPickSerializer

    def get_queryset(self):
        owner = self.request.user
        team = UserTeam.objects.get(owner=owner)
        queryset = UserPick.objects.filter(team=team)
        return queryset
