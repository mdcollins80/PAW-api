from django.contrib import admin
from .models import UserPick
# Register your models here.

class UserPickAdmin(admin.ModelAdmin):
    list_display = ('team', 'game', 'pick')

admin.site.register(UserPick, UserPickAdmin)
