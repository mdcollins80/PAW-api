from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views
from rest_framework.routers import DefaultRouter

from paw2018.users.urls import api_router as user_router
from paw2018.leagues.urls import api_router as league_router
from paw2018.userteams.urls import api_router as userteam_router
from paw2018.userpicks.urls import api_router as userpick_router
from paw2018.nflteams.urls import api_router as team_router
from paw2018.nflgames.urls import api_router as game_router

class MasterRouter(DefaultRouter):
    def register_subrouter(self, subrouter):
        self.registry.extend(subrouter.registry)

api_router = MasterRouter()
api_router.register_subrouter(user_router)
api_router.register_subrouter(league_router)
api_router.register_subrouter(userteam_router)
api_router.register_subrouter(userpick_router)
api_router.register_subrouter(team_router)
api_router.register_subrouter(game_router)

urlpatterns = [
    path("", TemplateView.as_view(template_name="pages/home.html"), name="home"),
    path(
        "about/",
        TemplateView.as_view(template_name="pages/about.html"),
        name="about",
    ),
    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),
    # User management
    path(
        "users/",
        include("paw2018.users.urls", namespace="users"),
    ),
    path("accounts/", include("allauth.urls")),
    # Your stuff: custom urls includes go here

    #API stuff
    path("api/", include(api_router.urls)),
    path("api-auth/", include('rest_framework.urls', namespace='rest_framework')),
] + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
