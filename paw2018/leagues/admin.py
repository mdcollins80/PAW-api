from django.contrib import admin
from .models import League

# Register your models here.

class LeagueAdmin(admin.ModelAdmin):
    list_display = ['owner', 'league_name', 'league_picture',]

admin.site.register(League)
