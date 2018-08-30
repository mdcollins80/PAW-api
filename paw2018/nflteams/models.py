from django.db import models
from model_utils import Choices

CONFERENCE_CHOICES = Choices('AFC', 'NFC')
DIVISION_CHOICES = Choices('East', 'North', 'South', 'West')

# Create your models here.
class Team(models.Model):
    location = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    conference = models.CharField(choices=CONFERENCE_CHOICES, max_length=3)
    division = models.CharField(choices=DIVISION_CHOICES, max_length=10)

    @property
    def wins(self):
        return 0

    @property
    def losses(self):
        return 0

    @property
    def division_wins(self):
        return 0

    @property
    def division_losses(self):
        return 0
