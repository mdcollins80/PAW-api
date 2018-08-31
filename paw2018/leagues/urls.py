from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from .views import LeagueViewSet

api_router = routers.DefaultRouter()
api_router.register(r'leagues', LeagueViewSet)

app_name = 'leagues'
urlspatterns = [
    path("", include(api_router.urls))
]
