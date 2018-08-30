from django.db import models

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
        return self.team + '-' + self.pick
