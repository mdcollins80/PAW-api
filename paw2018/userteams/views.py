from rest_framework import viewsets
from .serializers import UserTeamSerializer
from .models import UserTeam

# Create your views here.
class UserTeamViewSet(viewsets.ModelViewSet):
    serializer_class = UserTeamSerializer
    def get_queryset(self):
        owner = self.request.user
        queryset = UserTeam.objects.all()
        myteam = self.request.query_params.get('myteam', None)
        if myteam is not None:
            queryset = queryset.filter(owner=owner)
        return queryset

# write a view that takes an argument for modifying the queryset
# so that it is either returning ALL objects, or it is returning
# just the user's team
