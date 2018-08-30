from django.db import models
from paw2018.users.models import User
from paw2018.leagues.models import League

# Create your models here.

class UserTeam(models.Model):
    owner = models.ForeignKey(User,
                              on_delete=models.CASCADE,
                              related_name='teams')
    league = models.ForeignKey(League,
                               on_delete=models.CASCADE,
                               related_name='teams')
    team_name = models.CharField(max_length=255)
    team_picture = models.ImageField(blank=True)

    def __str__(self):
        return self.team_name
