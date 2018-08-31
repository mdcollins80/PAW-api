from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from .views import UserPickViewSet

api_router = routers.DefaultRouter()
api_router.register(r'userpicks', UserPickViewSet)

app_name = 'userpicks'
urlspatterns = [
    path("", include(api_router.urls))
]
