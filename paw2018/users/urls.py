from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from .views import UserViewSet

from paw2018.users.views import (
    user_list_view,
    user_redirect_view,
    user_update_view,
    user_detail_view,
)

api_router = routers.DefaultRouter()
api_router.register(r'users', UserViewSet)

app_name = "users"
urlpatterns = [
    path("", include(api_router.urls)),
    path("", view=user_list_view, name="list"),
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("<str:username>/", view=user_detail_view, name="detail"),
]
