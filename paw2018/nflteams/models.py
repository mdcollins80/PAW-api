from django.db import models
from model_utils import Choices



# Create your models here.
class Team(models.Model):
    CONFERENCE_CHOICES = Choices('AFC', 'NFC')
    DIVISION_CHOICES = Choices('East', 'North', 'South', 'West')
    location = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    conference = models.CharField(choices=CONFERENCE_CHOICES, max_length=3)
    division = models.CharField(choices=DIVISION_CHOICES, max_length=10)

    def __str__(self):
        return self.location + ' ' + self.name

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
