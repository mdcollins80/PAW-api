from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from .views import GameViewSet

api_router = routers.DefaultRouter()
api_router.register(r'games', GameViewSet)

app_name = 'nflgames'
urlspatterns = [
    path("", include(api_router.urls))
]
