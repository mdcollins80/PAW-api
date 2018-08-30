from django.db import models
from paw2018.users.models import User

# Create your models here.
class League(models.Model):
    owner = models.ForeignKey(User,
                              on_delete=models.CASCADE,
                              related_name='leagues')
    league_name = models.CharField(max_length=255)
    league_picture = models.ImageField(blank=True)

    def __str__(self):
        return self.league_name
