from rest_framework import viewsets
from .serializers import UserPickSerializer
from .models import UserPick

# Create your views here.
class UserPickViewSet(viewsets.ModelViewSet):
    queryset = UserPick.objects.all()
    serializer_class = UserPickSerializer
