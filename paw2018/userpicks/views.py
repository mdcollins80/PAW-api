from rest_framework import viewsets
from .serializers import UserPickSerializer, UserPickPostSerializer
from .models import UserPick

# Create your views here.
class UserPickViewSet(viewsets.ModelViewSet):
    queryset = UserPick.objects.all().prefetch_related('pick','game','team')
    serializer_class = UserPickSerializer


class UserPickPostSet(viewsets.ModelViewSet):
    serializer_class = UserPickPostSerializer
