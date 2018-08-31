from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from .views import TeamViewSet

api_router = routers.DefaultRouter()
api_router.register(r'teams', TeamViewSet)

app_name = 'nflteams'
urlspatterns = [
    path("", include(api_router.urls))
]
