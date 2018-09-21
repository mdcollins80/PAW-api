from django.db import models
from paw2018.nflteams.models import Team

# Create your models here.
class Game(models.Model):
    kickoff = models.DateTimeField()
    week_num = models.SmallIntegerField()
    home_team = models.ForeignKey(Team,
                                  on_delete=models.CASCADE,
                                  related_name="home_games")
    home_team_score = models.SmallIntegerField(blank=True,
                                               null=True)
    away_team = models.ForeignKey(Team,
                                  on_delete=models.CASCADE,
                                  related_name="away_games")
    away_team_score = models.SmallIntegerField(blank=True,
                                               null=True)

    def __str__(self):
        return self.away_team.name + ' @ ' + self.home_team.name

    @property
    def weekday(self):
        date = self.kickoff
        return date.strftime("%A")

    @property
    def season(self):
        date = self.kickoff
        if date.month >= 9:
            return str(date.year) + "-" + str(date.year + 1)
        else:
            return str(date.year - 1) + "-" + str(date.year)

    @property
    def winner(self):
        if isinstance(self.home_team_score, int) and isinstance(self.away_team_score, int):
            if self.home_team_score > self.away_team_score:
                return self.home_team.id
            elif self.home_team_score == self.away_team_score:
                return 0
            else:
                return self.away_team.id
