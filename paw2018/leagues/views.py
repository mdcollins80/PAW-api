from .models import League
from .serializers import LeagueSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, status

# Create your views here.

# class LeagueList(APIView):
#     def get(self, request, format=None):
#         leagues = League.objects.all()
#         serializer = LeagueSerializer(leagues, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = LeagueSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LeagueViewSet(viewsets.ModelViewSet):
    queryset = League.objects.all()
    serializer_class = LeagueSerializer
