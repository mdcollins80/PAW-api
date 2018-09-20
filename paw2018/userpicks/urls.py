from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from .views import UserPickViewSet, UserPickPostSet

api_router = routers.DefaultRouter()
api_router.register(r'userpicks', UserPickViewSet)
api_router.register(r'userpicksPost', UserPickPostSet, 'userpickPost')

app_name = 'userpicks'
urlspatterns = [
    path("", include(api_router.urls))
]
