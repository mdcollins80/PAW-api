from django.contrib import admin
from .models import UserTeam, League

# Register your models here.
class UserTeamAdmin(admin.ModelAdmin):
    list_display = ('league', 'owner', 'team_name')
    list_filter = ('league', 'owner', 'team_name')

    # def league_name(self, obj):
    #     return obj.league.league_name

admin.site.register(UserTeam, UserTeamAdmin)
