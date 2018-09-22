from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from .views import UserTeamViewSet, UserTeamOwned

api_router = routers.DefaultRouter()
api_router.register(r'userteams', UserTeamViewSet, 'userteam')

app_name = 'userteams'
urlspatterns = [
    path("", include(api_router.urls)),
]
