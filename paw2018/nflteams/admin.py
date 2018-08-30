from django.contrib import admin
from .models import Team

# Register your models here.
class TeamAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'conference', 'division',
                    'wins', 'losses', 'division_wins', 'division_losses')
    list_filter = ('conference', 'division')

admin.site.register(Team, TeamAdmin)
