from django.contrib import admin
from .models import Game

# Register your models here.
class GameAdmin(admin.ModelAdmin):
    list_display = ('week_num', 'weekday', 'kickoff', 'away_team',
                    'away_team_score', 'home_team', 'home_team_score')
    list_filter = ('week_num', 'away_team', 'home_team')

admin.site.register(Game, GameAdmin)
