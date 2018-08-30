from django.db import models
from paw2018.nflteams.models import Team

# Create your models here.
class Game(models.Model):
    kickoff = models.DateTimeField()
    week_num = models.SmallIntegerField()
    home_team = models.ForeignKey(Team,
                                  on_delete=models.CASCADE,
                                  related_name="home_games")
    home_team_score = models.SmallIntegerField()
    away_team = models.ForeignKey(Team,
                                  on_delete=models.CASCADE,
                                  related_name="away_games")
    away_team_score = models.SmallIntegerField()

    def __str__(self):
        return self.home_team + '@ ' + self.away_team

    @property
    def season(self):
        date = self.kickoff
        if date.month >= 9:
            return str(date.year) + "-" + str(date.year + 1)
        else:
            return str(date.year - 1) + "-" + str(date.year)
