from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from .views import UserPickViewSet, UserPickPostSet, UserPickOwned

api_router = routers.DefaultRouter()
api_router.register(r'userpicks', UserPickViewSet)
api_router.register(r'userpicksPost', UserPickPostSet, 'userpickPost')
api_router.register(r'userpicksOwned', UserPickOwned, 'userpickOwned')

app_name = 'userpicks'
urlspatterns = [
    path("", include(api_router.urls))
]
