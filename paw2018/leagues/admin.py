from django.contrib import admin
from .models import League

# Register your models here.

class LeagueAdmin(admin.ModelAdmin):
    list_display = ('owner', 'league_name')
    list_filter = ('owner', )

admin.site.register(League, LeagueAdmin)
