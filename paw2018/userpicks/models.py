from django.db import models
from paw2018.userteams.models import UserTeam
from paw2018.nflgames.models import Game
from paw2018.nflteams.models import Team

# Create your models here.
class UserPick(models.Model):
    team = models.ForeignKey(UserTeam,
                             on_delete=models.CASCADE,
                             related_name='userpicks')
    game = models.ForeignKey(Game,
                             on_delete=models.CASCADE,
                             related_name='userpicks')
    pick = models.ForeignKey(Team,
                             on_delete=models.CASCADE,
                             related_name='userpicks')

    def __str__(self):
        return self.team.team_name + '-' + self.pick.name

    def correct(self):
        if self.game.winner and self.game.winner == self.pick.id:
            return 1
        elif self.game.winner:
            return 0
